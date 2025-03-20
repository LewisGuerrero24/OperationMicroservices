import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { CategoryModule } from './category/category.module'; // Importar módulo de categorías
import { Category } from './category/entities/category.entity';
import { CategoryController } from './category/category.controller';
import { ProductsModule } from './products/products.module';
import { Product } from './products/entities/product.entity';
import { CategoryService } from './category/category.service';
import { ProductsService } from './products/products.service';
import { WareHouseModule } from './ware-house/ware-house.module';
import { InventoryModule } from './inventory/inventory.module';
import { InventoryMovementModule } from './inventory-movement/inventory-movement.module';
import { InventoryController } from './inventory/inventory.controller';
import { InventoryMovementController } from './inventory-movement/inventory-movement.controller';
import { InventoryMovementService } from './inventory-movement/inventory-movement.service';
import { InventoryService } from './inventory/inventory.service';
import { WareHouseController } from './ware-house/ware-house.controller';
import { WareHouseService } from './ware-house/ware-house.service';
import { Inventory } from './inventory/entities/inventory.entity';
import { WareHouse } from './ware-house/entities/ware-house.entity';
import { InventoryMovement } from './inventory-movement/entities/inventory-movement.entity';

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'mssql', // Tipo de base de datos
      host: 'localhost', // Servidor SQL
      port: 1433, // Puerto por defecto de SQL Server
      username: 'sa',
      password: 'Aramis21',
      database: 'SGI',
      entities: [Category,Product, Inventory,WareHouse, InventoryMovement], // Importar entidad correctamente
      synchronize: true, // ⚠️ Solo en desarrollo, desactívalo en producción
      extra: {
        options: {
          encrypt: false, // ⚠️ Importante para conexiones locales, cambiar a true en producción
          trustServerCertificate: true, // Evita problemas de certificado en localhost
        },
      },
    }),
    TypeOrmModule.forFeature([Category,Product]), // Registrar la entidad en el módulo principal
    CategoryModule, ProductsModule, WareHouseModule, InventoryModule, InventoryMovementModule,
  ],
  controllers: [CategoryController, InventoryController, InventoryMovementController, WareHouseController],
  providers: [CategoryService, ProductsService, InventoryMovementService, InventoryService, WareHouseService],
})
export class AppModule {}
