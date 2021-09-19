namespace Organizer.Settings
{
    public class RabbitMQSettings
    {
        public string Username { get; set; }
        public string Password { get; set; }
        public string VirtualHost { get; set; }
        public string HostName { get; set; }
        public string QueuePublishName { get; set; }
    }
}