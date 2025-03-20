// using Application.Service;
// using Domain.Ports;
// using Infrastructure.Adapters;
using Infrastructure.Data;
using Microsoft.EntityFrameworkCore;


var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllers();
// builder.Services.AddScoped<PruebaService>();
// builder.Services.AddScoped<IPruebaRepository,PruebaRepository>();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddDbContext<MyContext>(
    options => options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection"),   
 
        b => b.MigrationsAssembly("Infrastructure")));


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
