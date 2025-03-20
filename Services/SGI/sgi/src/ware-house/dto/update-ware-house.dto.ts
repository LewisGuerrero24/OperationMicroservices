import { PartialType } from '@nestjs/mapped-types';
import { CreateWareHouseDto } from './create-ware-house.dto';

export class UpdateWareHouseDto extends PartialType(CreateWareHouseDto) {}
