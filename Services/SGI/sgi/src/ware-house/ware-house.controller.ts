import { Controller, Get, Post, Body, Patch, Param, Delete } from '@nestjs/common';
import { WareHouseService } from './ware-house.service';
import { CreateWareHouseDto } from './dto/create-ware-house.dto';
import { UpdateWareHouseDto } from './dto/update-ware-house.dto';

@Controller('ware-house')
export class WareHouseController {
  constructor(private readonly wareHouseService: WareHouseService) {}

  @Post()
  create(@Body() createWareHouseDto: CreateWareHouseDto) {
    return this.wareHouseService.create(createWareHouseDto);
  }

  @Get()
  findAll() {
    return this.wareHouseService.findAll();
  }

  @Get(':id')
  findOne(@Param('id') id: string) {
    return this.wareHouseService.findOne(+id);
  }

  @Patch(':id')
  update(@Param('id') id: string, @Body() updateWareHouseDto: UpdateWareHouseDto) {
    return this.wareHouseService.update(+id, updateWareHouseDto);
  }

  @Delete(':id')
  remove(@Param('id') id: string) {
    return this.wareHouseService.remove(+id);
  }
}
