import { Column } from "typeorm";

export class CreateWareHouseDto {
        @Column()
        nombre_almacen: string;
      
        @Column()
        ciudad: string;
      
        @Column()
        direccion: string;
      
        @Column()
        telefono: string;
}
