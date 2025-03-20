using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using System.Threading.Tasks;
using Application.Services.Kafka;
using Domain.Entities;
using Domain.Entities.Kafka;
using Microsoft.AspNetCore.Mvc;

namespace Api.Controller
{
    [ApiController]
    [Route("api/[controller]")]
    public class KafkaControllerProducer : ControllerBase
    {
        private readonly PruebaKafkaServices _kafkaService;

        private readonly ILogger<KafkaControllerProducer> _logger;

        public KafkaControllerProducer(PruebaKafkaServices kafkaService, ILogger<KafkaControllerProducer> logger)
        {
            _kafkaService = kafkaService;
            _logger = logger;
        }

        [HttpPost("send")]
        public async Task<IActionResult> SendMessage([FromBody] Prueba request)
        {
            var message = JsonSerializer.Serialize(request);

            await _kafkaService.SendMessages(KafkaTopics.INVENTORY_UPDATE,message);

            return Ok("Message Succeful...");
            
        }

       
        }

       
       
    }
