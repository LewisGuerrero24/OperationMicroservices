import { ApiProperty } from "@nestjs/swagger";

export class CreateInventoryDto {

      
        @ApiProperty({ example:0, description: 'Producto_Id', required: true })
        producto: number;
      
        @ApiProperty({ example:0, description: 'WareHouse_Id', required: true })
        almacen: number;
      
        @ApiProperty({ example:0, description: 'Cantidad', required: true })
        cantidad: number;

}
