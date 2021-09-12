using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using AlgorithmConfigDbClient.Entities;
using Entities;
using Microsoft.Extensions.Logging;
using MongoDB.Bson;
using MongoDB.Driver;

namespace AlgorithmConfigDbClient
{
    public class AlgorithmConfigsService
    {
        private readonly ILogger<AlgorithmConfigsService> _logger;
        private readonly IMongoCollection<AlgorithmConfigEntity> _configs;
        private readonly AlgorithmConfigsServiceSettings _settings;
        public IMongoDatabase Database { get; set; }


        public AlgorithmConfigsService(ILogger<AlgorithmConfigsService> logger, AlgorithmConfigsServiceSettings settings)
        {
            _logger = logger;
            _settings = settings;
            var credential = MongoCredential.CreateCredential(
                settings.DatabaseName,
                settings.Username,
                settings.Password
            );
            var host = new MongoServerAddress(settings.Host);

            var mongoClientSettings = new MongoClientSettings
            {
                Credential = credential,
                Server = host,
                UseTls = false
            };
            var client = new MongoClient(mongoClientSettings);
            var db = client.GetDatabase(settings.DatabaseName);
            _configs = db.GetCollection<AlgorithmConfigEntity>("AlgorithmConfig");
        }

        public async Task<IList<AlgorithmConfig>> Get()
        {
            var report = await _configs.Find(c => true).ToListAsync();
            return convert(report);
        }

        public async Task UpdateLastRun(string id, DateTime lastRun)
        {
            _logger.LogTrace($"Updating algorithm config: {id}, to last-ran: {lastRun}");
            var update = Builders<AlgorithmConfigEntity>.Update.Set("LastRun", lastRun);
            await _configs.UpdateOneAsync<AlgorithmConfigEntity>(r => r.Id == id, update);
        }

        private IList<AlgorithmConfig> convert(List<AlgorithmConfigEntity> entity)
        {
            return entity?.Select(e => convert(e)).ToList();
        }

        private AlgorithmConfig convert(AlgorithmConfigEntity entity)
        {
            return new AlgorithmConfig(
                entity.Id,
                entity.Algorithm,
                entity.RunIntervalMinutes,
                entity.DataPeriodeDays,
                entity.Customer,
                entity.Tags,
                entity.LastRun
            );
        }
    }
}
