import { Injectable } from '@nestjs/common';
import { CreateWareHouseDto } from './dto/create-ware-house.dto';
import { UpdateWareHouseDto } from './dto/update-ware-house.dto';
import { InjectRepository } from '@nestjs/typeorm';
import { WareHouse } from './entities/ware-house.entity';
import { Repository } from 'typeorm';
import { error } from 'console';

@Injectable()
export class WareHouseService {

constructor(
    @InjectRepository(WareHouse) // Asegura la inyección correcta
    private readonly wareHouseRepository: Repository<WareHouse>,
  ) {}


  
  async create(createWareHouseDto: CreateWareHouseDto):Promise<WareHouse> {

    return await this.wareHouseRepository.save(createWareHouseDto);
  }

  async findAll():Promise<WareHouse[]> {
    return  await this.wareHouseRepository.find()
  }

  async findOne(id_almacen: number):Promise<WareHouse>{
    var dataUnique = await this.wareHouseRepository.findOne({where: {id_almacen}})
    if(!dataUnique){
      throw new error ("ERROR DATA almacen")
    }
    return dataUnique;
  }

  async update(id: number, updateWareHouseDto: UpdateWareHouseDto) {
    await this.wareHouseRepository.update(id,updateWareHouseDto);
    return this.findOne(id)
  }

  async remove(id: number) {
    await this.wareHouseRepository.delete(id);
  }
}
