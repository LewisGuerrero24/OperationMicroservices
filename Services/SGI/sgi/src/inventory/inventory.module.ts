import { Module } from '@nestjs/common';
import { InventoryService } from './inventory.service';
import { InventoryController } from './inventory.controller';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Product } from 'src/products/entities/product.entity';
import { WareHouse } from 'src/ware-house/entities/ware-house.entity';
import { Inventory } from './entities/inventory.entity';

@Module({
  imports: [TypeOrmModule.forFeature([Inventory,Product,WareHouse])], // Registra el repositorio en el módulo
  providers: [InventoryService],
  controllers: [InventoryController],
  exports: [InventoryService],
})
export class InventoryModule {}

