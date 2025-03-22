import { Injectable } from '@nestjs/common';
import { CreateProductDto } from './dto/create-product.dto';
import { UpdateProductDto } from './dto/update-product.dto';
import { InjectRepository } from '@nestjs/typeorm';
import { Product } from './entities/product.entity';
import { Repository } from 'typeorm';
import { error } from 'console';
import { Category } from 'src/category/entities/category.entity';

@Injectable()
export class ProductsService {

  constructor(
    @InjectRepository(Product) // Asegura la inyección correcta
    private readonly productRepository: Repository<Product>,

    @InjectRepository(Category)
    private categoryRepository: Repository<Category>,
  ) {}

  async create(createProductDto: CreateProductDto):Promise<Product> {

    const category = await this.categoryRepository.findOne({
      where: { id_categoria: createProductDto.categoria },
    });

    if (!category) {
      throw new Error('Categoría no encontrada');
    }

    const newProduct = this.productRepository.create({
      nombre_producto: createProductDto.nombre_producto,
      categoria: category, // Asignar el objeto de categoría encontrado
      precio_unitario: createProductDto.precio_unitario,
      stock: createProductDto.stock,
      codigo_identificacion: createProductDto.codigo_identificacion,
      status: createProductDto.status,
    });
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

    const category = await this.categoryRepository.findOne({
      where: { id_categoria: updateProductDto.categoria },
    });

    if (!category) {
      throw new Error('Categoría no encontrada');
    }

    const updateProduct = this.productRepository.create({
      nombre_producto: updateProductDto.nombre_producto,
      categoria: category, // Asignar el objeto de categoría encontrado
      precio_unitario: updateProductDto.precio_unitario,
      stock: updateProductDto.stock,
      codigo_identificacion: updateProductDto.codigo_identificacion,
      status: updateProductDto.status,
    });
    await this.productRepository.update(id,updateProduct);
    return this.findOne(id);
  }

  async remove(id: number) {
    await this.productRepository.delete(id)
  }
}
