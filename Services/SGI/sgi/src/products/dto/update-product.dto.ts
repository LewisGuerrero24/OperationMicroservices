import { PartialType } from '@nestjs/mapped-types';
import { CreateProductDto } from './create-product.dto';
import { ApiProperty } from '@nestjs/swagger';
import { Category } from 'src/category/entities/category.entity';

export class UpdateProductDto extends PartialType(CreateProductDto) {
            @ApiProperty({ example: 'nombreProducto', description: 'Nombre', required: true })
            nombre_producto: string;
          
            @ApiProperty({ example: Category, description: 'Categoria', required: true })
            categoria: Category;
          
            @ApiProperty({ example: 0.0,description: 'Precio', required: true })
            precio_unitario: number;
          
            @ApiProperty({ example: 0,description: 'Cantidad', required: true })
            stock: number;
          
            @ApiProperty({ example: 'codigo_producto',description: 'Codigo_Producto', required: true })
            codigo_identificacion: number;
          
            @ApiProperty({ example: 'Estado_Producto',description: 'Estado', required: true })
            status: string;
}
