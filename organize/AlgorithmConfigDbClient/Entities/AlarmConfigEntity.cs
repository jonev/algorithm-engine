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
        public List<string> Tags { get; set; } // TODO denne må være en liste med en liste, slik at hver algoritme kan ha flere tag, og denne kan inneholde flere jobber på samme algoritme
        public DateTime LastRun { get; set; }

        public AlgorithmConfigEntity(string id, string algorithm, int runIntervalMinutes, int dataPeriodeDays, string customer, List<string> tags, DateTime lastRun)
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