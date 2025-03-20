import { Product } from "src/products/entities/product.entity";
import { WareHouse } from "src/ware-house/entities/ware-house.entity";
import { Column, Entity, ManyToOne, PrimaryGeneratedColumn } from "typeorm";

@Entity()
export class Inventory {
    @PrimaryGeneratedColumn()
    id_inventario: number;
  
    @ManyToOne(() => Product, (producto) => producto.id_producto)
    producto: Product;
  
    @ManyToOne(() => WareHouse, (almacen) => almacen.id_almacen)
    almacen: WareHouse;
  
    @Column()
    cantidad: number;
}
