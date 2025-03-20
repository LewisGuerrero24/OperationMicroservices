using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Confluent.Kafka;
using Domain.Entities.Kafka;
using Domain.Ports.Ikafka;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging;

namespace Infrastructure.Adapters.Kafka
{
    public class KafkaConsumerRepository : IKafkaConsumer
{
    private readonly IConsumer<Ignore, string> _consumer;
    private readonly ILogger<KafkaConsumerRepository> _logger;
    private readonly IConfiguration _configuration;

    public KafkaConsumerRepository(ILogger<KafkaConsumerRepository> logger, IConfiguration configuration)
    {
        _logger = logger;
        _configuration = configuration;

        var consumerConfig = new ConsumerConfig
        {
            BootstrapServers = _configuration["Kafka:BootstrapServers"],
            GroupId = "pos",
            AutoOffsetReset = AutoOffsetReset.Earliest,
            EnableAutoCommit = false
        };

        _consumer = new ConsumerBuilder<Ignore, string>(consumerConfig).Build();
    }

    public async Task StartConsumingAsync(CancellationToken stoppingToken)
    {
        _consumer.Subscribe(KafkaTopics.INVENTORY_UPDATE);

        try
        {
            while (!stoppingToken.IsCancellationRequested)
            {
                ProcessKafkaMessage(stoppingToken);
                
            }
        }
        catch (OperationCanceledException)
        {
            _logger.LogInformation("Consuming canceled.");
        }
        finally
        {
            _consumer.Close();
            _logger.LogInformation("Consumer closed.");
        }
    }

    public void ProcessKafkaMessage(CancellationToken stoppingToken)
    {
        try
        {
            var consumeResult = _consumer.Consume(stoppingToken);

            if (consumeResult != null)
            {
                var message = consumeResult.Message.Value;
                _logger.LogInformation($"Received message at {consumeResult.TopicPartitionOffset}: {message}");

                // Commit manually after processing
                _consumer.Commit(consumeResult);
            }
        }
        catch (ConsumeException ex)
        {
            _logger.LogError($"Kafka consume error: {ex.Error.Reason}");
        }
        catch (Exception ex)
        {
            _logger.LogError($"General error processing Kafka message: {ex.Message}");
        }
    }
}

}