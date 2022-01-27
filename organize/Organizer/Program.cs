using AlgorithmConfigDbClient;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using Organizer.Services;
using Organizer.Settings;

namespace Organizer
{
    public class Program
    {
        public static void Main(string[] args)
        {
            CreateHostBuilder(args).Build().Run();
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureLogging(logging =>
                {
                    logging.ClearProviders();
                    logging.AddConsole();
                })
                .ConfigureServices((hostContext, services) =>
                {
                    IConfiguration configuration = hostContext.Configuration;

                    var algorithmConfigsServiceSettings = configuration.GetSection("AlgorithmConfigsServiceSettings").Get<AlgorithmConfigsServiceSettings>();
                    services.AddSingleton(algorithmConfigsServiceSettings);
                    var rabbitMQServiceSettings = configuration.GetSection("RabbitMQSettings").Get<RabbitMQSettings>();
                    services.AddSingleton(rabbitMQServiceSettings);

                    services.AddSingleton<AlgorithmConfigsService>();
                    services.AddSingleton<QueueService>();
                    services.AddHostedService<Worker>();
                });
    }
}
