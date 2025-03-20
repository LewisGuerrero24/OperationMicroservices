import { Module } from '@nestjs/common';
import { WareHouseService } from './ware-house.service';
import { WareHouseController } from './ware-house.controller';

@Module({
  controllers: [WareHouseController],
  providers: [WareHouseService],
})
export class WareHouseModule {}
