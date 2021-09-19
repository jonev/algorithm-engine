using System;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;
using Organizer.Entities;
using Organizer.Settings;
using RabbitMQ.Client;

namespace Organizer.Services
{
    public class QueueService : IDisposable
    {
        private readonly ILogger<QueueService> _logger;
        private readonly RabbitMQSettings _settings;
        private IConnection _conn;
        private IModel _channel;

        public QueueService(ILogger<QueueService> logger, RabbitMQSettings settings)
        {
            _logger = logger;
            this._settings = settings;
            ConnectionFactory factory = new ConnectionFactory();
            // "guest"/"guest" by default, limited to localhost connections
            factory.UserName = settings.Username;
            factory.Password = settings.Password;
            factory.VirtualHost = settings.VirtualHost;
            factory.HostName = settings.HostName;

            _conn = factory.CreateConnection();
            _channel = _conn.CreateModel();
        }

        public void PublishJob(Job job)
        {
            byte[] messageBodyBytes = System.Text.Encoding.UTF8.GetBytes(
                JsonConvert.SerializeObject(job, Formatting.Indented)
                );
            _channel.BasicPublish("", _settings.QueuePublishName, null, messageBodyBytes);
        }

        public void Dispose()
        {
            _channel?.Close();
            _conn?.Close();
        }
    }
}