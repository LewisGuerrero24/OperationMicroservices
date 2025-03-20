using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Application.useCases.Kafka
{
    public interface PruebaKafkaUseCase
    {
        Task SendMessages(string topic, string message);
    }
}