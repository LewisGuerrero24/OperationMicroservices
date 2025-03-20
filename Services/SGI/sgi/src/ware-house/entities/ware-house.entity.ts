import { Product } from "src/products/entities/product.entity";
import { Column, Entity, ManyToMany, PrimaryGeneratedColumn } from "typeorm";

@Entity()
export class WareHouse {
    @PrimaryGeneratedColumn()
    id_almacen: number;
  
    @Column()
    nombre_almacen: string;
  
    @Column()
    ciudad: string;
  
    @Column()
    direccion: string;
  
    @Column()
    telefono: string;
  
    @ManyToMany(() => Product, (producto) => producto.almacenes)
    productos: Product[];
}
