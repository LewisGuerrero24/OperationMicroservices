import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { ProductsService } from './products.service';
import { ProductsController } from './products.controller';
import { Product } from './entities/product.entity';

@Module({
  imports: [TypeOrmModule.forFeature([Product])], // Registra el repositorio en el módulo
  providers: [ProductsService],
  controllers: [ProductsController],
  exports: [ProductsService], // Exporta si se usa en otro módulo
})
export class ProductsModule {}