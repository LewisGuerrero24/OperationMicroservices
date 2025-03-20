import { ApiProperty } from "@nestjs/swagger";

export class CreateCategoryDto {
  @ApiProperty({ example: 'producto_categoria', description: 'Nombre_Categoria', required: true })
  nombre_categoria: string;
}
