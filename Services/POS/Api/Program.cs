using Application.Services;
using Application.Services.Kafka;
using Confluent.Kafka;
using Domain.Ports;
using Domain.Ports.Ikafka;
using Infrastructure.Adapters;
using Infrastructure.Adapters.Kafka;
using Infrastructure.Data;
using Microsoft.EntityFrameworkCore;


var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllers();

// var producerConfig = new ProducerConfig();
// builder.Configuration.Bind("Kafka:BootstrapServers", producerConfig); 

// var consumerConfig = new ConsumerConfig();
// builder.Configuration.Bind("Kafka:ConsumerConfig", consumerConfig);

// // Registrar las configuraciones de Kafka en el contenedor de servicios
// builder.Services.AddSingleton(producerConfig);
// builder.Services.AddSingleton(consumerConfig);


builder.Services.AddScoped<PruebaService>();
builder.Services.AddScoped<IPruebaRepository,PruebaRepository>();
builder.Services.AddScoped<CustomerServices>();
builder.Services.AddScoped<ICustomerRepository,CustomerRepository>();
builder.Services.AddScoped<BranchServices>();
builder.Services.AddScoped<IBranchRepository,BranchRepository>();
builder.Services.AddSingleton<IKafkaConsumer, KafkaConsumerRepository>();
builder.Services.AddScoped<IKafkaProducer, KafkaProducerRepository>();
builder.Services.AddScoped<PruebaKafkaServices>();
builder.Services.AddHostedService<KafkaConsumerServices>();

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

//conexion
builder.Services.AddDbContext<MyContext>(
    options => options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection"),   
 
        b => b.MigrationsAssembly("Infrastructure"))
        
        );


var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers(); // Asegúrate de mapear los controladores

app.Run();
