import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { CategoryService } from './category.service';
import { CategoryController } from './category.controller';
import { Category } from './entities/category.entity';

@Module({
  imports: [TypeOrmModule.forFeature([Category])], // 👈 IMPORTANTE
  providers: [CategoryService],
  controllers: [CategoryController],
  exports: [CategoryService], // 👈 Exportar si otros módulos lo usan
})
export class CategoryModule {}
