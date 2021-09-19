using System;
using System.Collections.Generic;
using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace AlgorithmConfigDbClient.Entities
{
    public class AlgorithmConfigEntity
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string Id { get; set; }
        public string Algorithm { get; set; }
        public int RunIntervalMinutes { get; set; }
        public int DataPeriodeDays { get; set; }
        public string Customer { get; set; }
        public IList<IList<string>> Tags { get; set; }
        public DateTime LastRun { get; set; }

        public AlgorithmConfigEntity(string id, string algorithm, int runIntervalMinutes, int dataPeriodeDays, string customer, IList<IList<string>> tags, DateTime lastRun)
        {
            Id = id;
            Algorithm = algorithm;
            RunIntervalMinutes = runIntervalMinutes;
            DataPeriodeDays = dataPeriodeDays;
            Customer = customer;
            Tags = tags;
            LastRun = lastRun;
        }
    }
    
}