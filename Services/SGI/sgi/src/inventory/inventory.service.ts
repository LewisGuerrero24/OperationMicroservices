import { Injectable } from '@nestjs/common';
import { CreateInventoryDto } from './dto/create-inventory.dto';
import { UpdateInventoryDto } from './dto/update-inventory.dto';
import { Inventory } from './entities/inventory.entity';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { error } from 'console';
import { Product } from 'src/products/entities/product.entity';
import { WareHouse } from 'src/ware-house/entities/ware-house.entity';
import { UpdateProductDto } from 'src/products/dto/update-product.dto';
import { UpdateCategoryDto } from 'src/category/dto/update-category.dto';

@Injectable()
export class InventoryService {

  constructor(
      @InjectRepository(Inventory) // Asegura la inyección correcta
      private readonly inventoryRepository: Repository<Inventory>,

      @InjectRepository(Inventory) // Asegura la inyección correcta
      private readonly productRepository: Repository<Product>,

      @InjectRepository(WareHouse) // Asegura la inyección correcta
      private readonly wareHouseRepository: Repository<WareHouse>,

    ) {}

  async create(createInventoryDto: CreateInventoryDto):Promise<Inventory> {
    const product = await this.productRepository.findOne({
      where: { id_producto: createInventoryDto.producto },
    });

    const wareHouse = await this.wareHouseRepository.findOne({
      where: { id_almacen: createInventoryDto.almacen },
    });

    if (!product ) {
      throw new Error('Categoría no encontrada');
    }

    if (!wareHouse ) {
      throw new Error('Categoría no encontrada');
    }

    const newProduct = this.inventoryRepository.create({
      producto: product,
      almacen: wareHouse,
      cantidad: createInventoryDto.cantidad 
    });
    return await this.inventoryRepository.save(newProduct);
  }

  async findAll():Promise<Inventory[]>  {
      return await this.inventoryRepository.find()
  }

  async findOne(id_inventario: number):Promise<Inventory> {
    var dtaInventory = await this.inventoryRepository.findOne({where: {id_inventario}})
    if(!dtaInventory){
      throw new error ("ERROR DATA Inventory")
    }
    return dtaInventory;
  }

  async  update(id: number, updateInventoryDto: UpdateInventoryDto) {
    const product = await this.productRepository.findOne({
      where: { id_producto: updateInventoryDto.producto },
    });

    const wareHouse = await this.wareHouseRepository.findOne({
      where: { id_almacen: updateInventoryDto.almacen },
    });

    if (!product ) {
      throw new Error('Categoría no encontrada');
    }

    if (!wareHouse ) {
      throw new Error('Categoría no encontrada');
    }

    const updateInventory = this.inventoryRepository.create({
      producto: product,
      almacen: wareHouse,
      cantidad: updateInventoryDto.cantidad 
    });
    await this.inventoryRepository.update(id,updateInventory);
    return this.findOne(id);
  }

  async remove(id: number) {
    await this.inventoryRepository.delete(id)
  }
}
