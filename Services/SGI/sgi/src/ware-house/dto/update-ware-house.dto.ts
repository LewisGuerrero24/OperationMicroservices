import { PartialType } from '@nestjs/mapped-types';
import { CreateWareHouseDto } from './create-ware-house.dto';
import { Column } from 'typeorm';

export class UpdateWareHouseDto extends PartialType(CreateWareHouseDto) {
            @Column()
            nombre_almacen: string;
          
            @Column()
            ciudad: string;
          
            @Column()
            direccion: string;
          
            @Column()
            telefono: string;
}
