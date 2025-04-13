import { Module } from '@nestjs/common';
import { WareHouseService } from './ware-house.service';
import { WareHouseController } from './ware-house.controller';
import { TypeOrmModule } from '@nestjs/typeorm';
import { WareHouse } from './entities/ware-house.entity';

@Module({
  imports: [TypeOrmModule.forFeature([WareHouse])], // Registra el repositorio en el módulo
  controllers: [WareHouseController],
  providers: [WareHouseService],
  exports:[WareHouseService]
})
export class WareHouseModule {}

