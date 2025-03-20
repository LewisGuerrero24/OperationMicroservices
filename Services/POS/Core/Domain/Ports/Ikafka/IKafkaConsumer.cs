using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Threading.Tasks;

namespace Domain.Ports.Ikafka
{
    public interface IKafkaConsumer
    {
        Task StartConsumingAsync(CancellationToken cancellationToken);
    }
}