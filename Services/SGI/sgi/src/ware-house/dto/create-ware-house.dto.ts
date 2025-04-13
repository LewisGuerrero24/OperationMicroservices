import { ApiProperty } from "@nestjs/swagger";
import { Column } from "typeorm";

export class CreateWareHouseDto {
        @ApiProperty({ example: 'nombreAlmacen', description: 'Nombre', required: true })
        nombre_almacen: string;
      
        @ApiProperty({example:'ciudad',description:'ubicacion', required:true})
        ciudad: string;
      
        @ApiProperty({example:'direccion',description:'direccion', required:true})
        direccion: string;
      
        @ApiProperty({example:'telefono', description:'numero de telefono', required:true })
        telefono: string;
}
