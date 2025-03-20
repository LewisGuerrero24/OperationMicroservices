using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Domain.Ports.Ikafka
{
    public interface IKafkaProducer
    {
         Task SendMessageAsync(string topic, string message);
    }
}