using System;
using System.Collections.Generic;

namespace Organizer.Entities
{
    public class Job
    {
        public string Id { get; set; }
        public string Algorithm { get; set; }
        public DateTime Start  { get; set; }
        public DateTime End  { get; set; }
        
        public IList<string> Tags { get; set; }



        public Job(string id, string algorithm, DateTime start, DateTime end, IList<string> tags)
        {
            Id = id;
            Algorithm = algorithm;
            Start = start;
            End = end;
            Tags = tags;
        }

        public override string ToString()
        {
            return $"{Id}, {Algorithm}, {Start}, {End}, {string.Join(",", Tags)}";
        }
    }
}