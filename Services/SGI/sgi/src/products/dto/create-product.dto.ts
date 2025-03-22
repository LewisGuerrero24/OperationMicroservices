import { ApiProperty } from "@nestjs/swagger";
import { Category } from "src/category/entities/category.entity";
import { Product } from "../entities/product.entity";

export class CreateProductDto {
        @ApiProperty({ example: 'nombreProducto', description: 'Nombre', required: true })
        nombre_producto: string;
      
        @ApiProperty({ example:0, description: 'Categoria', required: true })
        categoria: number;
      
        @ApiProperty({ example: 0.0,description: 'Precio', required: true })
        precio_unitario: number;
      
        @ApiProperty({ example: 0,description: 'Cantidad', required: true })
        stock: number;
      
        @ApiProperty({ example: 'codigo_producto',description: 'Codigo_Producto', required: true })
        codigo_identificacion: string;
      
        @ApiProperty({ example: 'Estado_Producto',description: 'Estado', required: true })
        status: string;
      
}
