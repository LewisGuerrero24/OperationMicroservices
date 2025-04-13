import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { DocumentBuilder, SwaggerModule } from '@nestjs/swagger';
import { Logger, LogLevel } from '@nestjs/common';
import { APP_IS_PROD } from 'config/envs';

async function bootstrap() {
  const logger = new Logger('bootstrap');
  const logLevel: LogLevel[] = ['error', 'warn', 'log'];

  if (!APP_IS_PROD) {
    logLevel.push('debug', 'verbose');  
  }

  const app = await NestFactory.create(AppModule, { logger: logLevel });

  // Configuración de Swagger
  const config = new DocumentBuilder()
    .setTitle('API de Ejemplo')
    .setDescription('Documentación de la API con Swagger en NestJS')
    .setVersion('1.0')
    .addBearerAuth()
    .build();

  const document = SwaggerModule.createDocument(app, config);
  SwaggerModule.setup('api/docs', app, document);

  await app.listen(3000);
  logger.log(`Aplicación corriendo en http://localhost:3000`);
}
bootstrap();

