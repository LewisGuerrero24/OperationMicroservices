using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Confluent.Kafka;
using Domain.Ports.Ikafka;
using Microsoft.Extensions.Configuration;

namespace Infrastructure.Adapters.Kafka
{
    public class KafkaProducerRepository : IKafkaProducer
    {
    

        private readonly IConfiguration _configuration;

        private readonly IProducer<Null, string> _producer;

        public KafkaProducerRepository(IConfiguration configuration)
        {
            _configuration = configuration;
            var producerconfig = new ProducerConfig
            {
                BootstrapServers = _configuration["Kafka:BootstrapServers"]
            };
            _producer = new ProducerBuilder<Null, string>(producerconfig).Build();;
        }

        public async Task SendMessageAsync(string topic, string message)
        {
           var kafkamessage = new Message<Null, string> { Value = message, };

            await _producer.ProduceAsync(topic, kafkamessage);
        }
    }
}