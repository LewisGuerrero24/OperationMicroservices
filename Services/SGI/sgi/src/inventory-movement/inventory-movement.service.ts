import { Injectable } from '@nestjs/common';
import { CreateInventoryMovementDto } from './dto/create-inventory-movement.dto';
import { UpdateInventoryMovementDto } from './dto/update-inventory-movement.dto';
import { InjectRepository } from '@nestjs/typeorm';
import { InventoryMovement } from './entities/inventory-movement.entity';
import { Repository } from 'typeorm';
import { Product } from 'src/products/entities/product.entity';
import { WareHouse } from 'src/ware-house/entities/ware-house.entity';
import { error } from 'console';

@Injectable()
export class InventoryMovementService {

  constructor(
    @InjectRepository(InventoryMovement)
    private readonly inventoryMovementRepository: Repository<InventoryMovement>,

    @InjectRepository(Product)
    private readonly productRepository: Repository<Product>,

    @InjectRepository(WareHouse)
    private readonly wareHouseRepository: Repository<WareHouse>
  ){}

async create(createInventoryMovementDto: CreateInventoryMovementDto):Promise<InventoryMovement> {
  const product = await this.productRepository.findOne({
    where: { id_producto: createInventoryMovementDto.producto },
  });

  const wareHouse = await this.wareHouseRepository.findOne({
    where: { id_almacen: createInventoryMovementDto.almacen },
  });

  if (!product ) {
    throw new Error('Categoría no encontrada');
  }

  if (!wareHouse ) {
    throw new Error('Categoría no encontrada');
  }

  const newMovement = this.inventoryMovementRepository.create({
    producto: product,
    almacen: wareHouse,
    tipo_movimiento: createInventoryMovementDto.tipo_movimiento,
    cantidad: createInventoryMovementDto.cantidad,
    razon: createInventoryMovementDto.razon,
    realizado_por_user: createInventoryMovementDto.realizado_por_user
  });
  return await this.inventoryMovementRepository.save(newMovement);
  }

  async findAll():Promise<InventoryMovement[]> {
    return await this.inventoryMovementRepository.find()
  }

  async findOne(id_movimiento: number):Promise<InventoryMovement> {
    var dtaMovement = await this.inventoryMovementRepository.findOne({where: {id_movimiento}})
    if(!dtaMovement){
      throw new error ("ERROR DATA Movement")
    }
    return dtaMovement;
  }

  async update(id: number, updateInventoryMovementDto: UpdateInventoryMovementDto) {
    const product = await this.productRepository.findOne({
      where: { id_producto: updateInventoryMovementDto.producto },
    });
  
    const wareHouse = await this.wareHouseRepository.findOne({
      where: { id_almacen: updateInventoryMovementDto.almacen },
    });
  
    if (!product ) {
      throw new Error('Categoría no encontrada');
    }
  
    if (!wareHouse ) {
      throw new Error('Categoría no encontrada');
    }
  
    const updateMovement = this.inventoryMovementRepository.create({
      producto: product,
      almacen: wareHouse,
      tipo_movimiento: updateInventoryMovementDto.tipo_movimiento,
      cantidad: updateInventoryMovementDto.cantidad,
      razon: updateInventoryMovementDto.razon,
      realizado_por_user: updateInventoryMovementDto.realizado_por_user
    });
    await this.inventoryMovementRepository.update(id,updateMovement);
    return this.findOne(id);
  }

  async remove(id: number) {
    await this.inventoryMovementRepository.delete(id)
  }
}
