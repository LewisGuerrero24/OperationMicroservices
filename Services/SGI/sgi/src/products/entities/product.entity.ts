import { Category } from "src/category/entities/category.entity";
import { WareHouse } from "src/ware-house/entities/ware-house.entity";
import { Column, Entity, JoinTable, ManyToMany, ManyToOne, PrimaryGeneratedColumn } from "typeorm";

@Entity()
export class Product { 
    @PrimaryGeneratedColumn()
    id_producto: number;
  
    @Column()
    nombre_producto: string;
  
    @ManyToOne(() => Category, (categoria) => categoria.productos)
    categoria: Category;
  
    @Column('decimal')
    precio_unitario: number;
  
    @Column()
    stock: number;
  
    @Column()
    codigo_identificacion: string;
  
    @Column()
    status: string;
  
    @ManyToMany(() => WareHouse, (almacen) => almacen.productos)
    @JoinTable()
    almacenes: WareHouse[];
}
