using System;

namespace Organizer.Entities
{
    public class Job
    {
        public string Id { get; set; }
        public string Algorithm { get; set; }
        public DateTime Start  { get; set; }
        public DateTime End  { get; set; }

        public Job(string id, string algorithm, DateTime start, DateTime end)
        {
            Id = id;
            Algorithm = algorithm;
            Start = start;
            End = end;
        }

        public override string ToString()
        {
            return $"{Id}, {Algorithm}, {Start}, {End}";
        }
    }
}