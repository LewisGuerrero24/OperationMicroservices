import { PartialType } from '@nestjs/mapped-types';
import { CreateWareHouseDto } from './create-ware-house.dto';
import { Column } from 'typeorm';
import { ApiProperty } from '@nestjs/swagger';

export class UpdateWareHouseDto extends PartialType(CreateWareHouseDto) {
                    @ApiProperty({ example: 'nombreAlmacen', description: 'Nombre', required: true })
                    nombre_almacen: string;
                  
                    @ApiProperty({example:'ciudad',description:'ubicacion', required:true})
                    ciudad: string;
                  
                    @ApiProperty({example:'direccion',description:'direccion', required:true})
                    direccion: string;
                  
                    @ApiProperty({example:'telefono', description:'numero de telefono', required:true })
                    telefono: string;
}
