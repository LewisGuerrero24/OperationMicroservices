import { Injectable } from '@nestjs/common';
import { CreateProductDto } from './dto/create-product.dto';
import { UpdateProductDto } from './dto/update-product.dto';
import { InjectRepository } from '@nestjs/typeorm';
import { Product } from './entities/product.entity';
import { Repository } from 'typeorm';
import { error } from 'console';

@Injectable()
export class ProductsService {

  constructor(
    @InjectRepository(Product) // Asegura la inyección correcta
    private readonly productRepository: Repository<Product>,
  ) {}

  async create(createProductDto: CreateProductDto):Promise<Product> {
    const newProduct = this.productRepository.create(createProductDto);
    return await this.productRepository.save(newProduct);
  }

  async findAll():Promise<Product[]>  {
    return await this.productRepository.find()
  }

  async findOne(id_producto: number):Promise<Product> {
    var dataUnique = await this.productRepository.findOne({where: {id_producto}})
    if(!dataUnique){
      throw new error ("ERROR DATA PRODUCT")
    }
    return dataUnique;
  }

  async update(id: number, updateProductDto: UpdateProductDto) {
    await this.productRepository.update(id,updateProductDto);
    return this.findOne(id);
  }

  async remove(id: number) {
    await this.productRepository.delete(id)
  }
}
