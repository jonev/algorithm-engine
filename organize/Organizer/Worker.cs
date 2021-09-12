using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using AlgorithmConfigDbClient;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using NCrontab;
using Organizer.Entities;

namespace Organizer
{
    public class Worker : BackgroundService
    {
        private readonly ILogger<Worker> _logger;
        private readonly AlgorithmConfigsService _config;
        private CrontabSchedule _schedule;

        private  string Schedule => "0 */1 * * * *"; //Runs every 1 minute

        public Worker(ILogger<Worker> logger, AlgorithmConfigsService config)
        {
            _logger = logger;
            _config = config;
            _schedule = CrontabSchedule.Parse(Schedule,new CrontabSchedule.ParseOptions { IncludingSeconds = true });
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            var nextrun = _schedule.GetNextOccurrence(DateTime.UtcNow);
            do
            {
                var now = DateTime.UtcNow;
                if (now > nextrun)
                {
                    #pragma warning disable 4014
                    Task.Factory.StartNew(async () => await Organize(nextrun))
                    .ContinueWith(t => {
                        switch (t.Status)
                        {
                            case TaskStatus.Created:
                            case TaskStatus.WaitingForActivation:
                            case TaskStatus.WaitingToRun:
                            case TaskStatus.Running:
                            case TaskStatus.WaitingForChildrenToComplete:
                            case TaskStatus.RanToCompletion:
                                break;
                            case TaskStatus.Canceled:
                            case TaskStatus.Faulted:
                                _logger.LogError("Failed run organizer task");
                                break;
                            default:
                                break;
                        }
                        
                    });
                    #pragma warning restore 4014
                    nextrun = _schedule.GetNextOccurrence(DateTime.UtcNow);
                }
                await Task.Delay(5000, stoppingToken); //5 seconds delay
            }
            while (!stoppingToken.IsCancellationRequested);
        }
        private async Task Organize(DateTime jobStart)
        {
            _logger.LogInformation($"--- Checking if any job should be created: {jobStart} ---");
            var configs = await _config.Get();
            foreach (var config in configs)
            {
                if(jobStart >= config.LastRun.AddMinutes(config.RunIntervalMinutes))
                {
                    foreach (var tag in config.Tags)
                    {
                        var job = new Job(
                            Guid.NewGuid().ToString(),
                            config.Algorithm,
                            jobStart,
                            jobStart.AddDays(-config.DataPeriodeDays)
                        );
                        _logger.LogInformation($"Job: {job}");
                        // TODO push the job to a queue
                    }
                    await _config.UpdateLastRun(config.Id, jobStart);
                }
            }
        }
    }
}
