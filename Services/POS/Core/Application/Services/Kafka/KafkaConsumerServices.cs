using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Domain.Ports.Ikafka;
using Microsoft.Extensions.Hosting;

namespace Application.Services.Kafka
{
    public class KafkaConsumerServices : IHostedService
    {
        private readonly IKafkaConsumer _kafkaConsumer;

        public KafkaConsumerServices(IKafkaConsumer kafkaConsumer)
        {
            _kafkaConsumer = kafkaConsumer;
        }

           public Task StartAsync(CancellationToken cancellationToken)
        {
            Task.Run(() => _kafkaConsumer.StartConsumingAsync(cancellationToken));
             return Task.CompletedTask;
        }

        public Task StopAsync(CancellationToken cancellationToken)
        {
             return Task.CompletedTask;
        }
    }
}