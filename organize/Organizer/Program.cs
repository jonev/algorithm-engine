using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using AlgorithmConfigDbClient;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

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
                .ConfigureServices((hostContext, services) =>
                {
                    IConfiguration configuration = hostContext.Configuration;

                    var algorithmConfigsServiceSettings = configuration.GetSection("AlgorithmConfigsServiceSettings").Get<AlgorithmConfigsServiceSettings>();

                    services.AddSingleton(algorithmConfigsServiceSettings);
                    services.AddSingleton<AlgorithmConfigsService>();
                    services.AddHostedService<Worker>();
                });
    }
}
