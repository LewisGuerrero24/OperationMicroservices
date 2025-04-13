import { Module } from '@nestjs/common';
import { InventoryMovementService } from './inventory-movement.service';
import { InventoryMovementController } from './inventory-movement.controller';
import { TypeOrmModule } from '@nestjs/typeorm';
import { InventoryMovement } from './entities/inventory-movement.entity';
import { Product } from 'src/products/entities/product.entity';
import { WareHouse } from 'src/ware-house/entities/ware-house.entity';

@Module({
  imports: [TypeOrmModule.forFeature([InventoryMovement, Product, WareHouse])],
  controllers: [InventoryMovementController],
  providers: [InventoryMovementService],
  exports:[InventoryMovementService]

})
export class InventoryMovementModule {}
