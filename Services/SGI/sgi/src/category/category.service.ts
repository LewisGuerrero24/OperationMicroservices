import { Injectable } from '@nestjs/common';
import { CreateCategoryDto } from './dto/create-category.dto';
import { UpdateCategoryDto } from './dto/update-category.dto';
import { Category } from './entities/category.entity';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';

@Injectable()
export class CategoryService {

  constructor(
    @InjectRepository(Category)
    private CategoryRepository: Repository<Category>,
  ) {}

  async create(createCategoryDto: CreateCategoryDto):Promise<Category>{
    const newProduct = this.CategoryRepository.create(createCategoryDto);
    return await this.CategoryRepository.save(newProduct);
  }

  async findAll():Promise<Category[]> {
    return await this.CategoryRepository.find();
  }

  async findOne(id_categoria: number):Promise<Category> {

    var data = await this.CategoryRepository.findOne({ where: { id_categoria } });

    if (!data) {
      throw new Error(`Category with ID ${id_categoria} not found`);
    }
    return data;
  }

  async update(id: number, updateCategoryDto: UpdateCategoryDto) {
    await this.CategoryRepository.update(id, updateCategoryDto);
    return this.findOne(id);
  }

  async remove(id: number) {
    await this.CategoryRepository.delete(id);
  }
}
