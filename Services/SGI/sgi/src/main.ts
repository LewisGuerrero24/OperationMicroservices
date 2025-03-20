import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { DataSource } from 'typeorm';
import { DocumentBuilder, SwaggerModule } from '@nestjs/swagger';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  // Configuración de Swagger
  const config = new DocumentBuilder()
    .setTitle('API de Ejemplo')
    .setDescription('Documentación de la API con Swagger en NestJS')
    .setVersion('1.0')
    .addBearerAuth() // Agrega autenticación por token si la necesitas
    .build();

  const document = SwaggerModule.createDocument(app, config);
  SwaggerModule.setup('api/docs', app, document); 


  await app.listen(3000);
}
bootstrap();
