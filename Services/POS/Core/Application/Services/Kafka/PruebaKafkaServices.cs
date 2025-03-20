using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Application.useCases.Kafka;
using Domain.Ports.Ikafka;
using Microsoft.Extensions.Hosting;

namespace Application.Services.Kafka
{
    public class PruebaKafkaServices : PruebaKafkaUseCase
    {
        private readonly IKafkaProducer _kafkaProducer;
        

        public PruebaKafkaServices(IKafkaProducer kafkaProducer)
        {
            _kafkaProducer = kafkaProducer;
        }

       

        public async Task SendMessages(string topic, string message)
        {
           await _kafkaProducer.SendMessageAsync(topic,message);
        }

     
    }
}