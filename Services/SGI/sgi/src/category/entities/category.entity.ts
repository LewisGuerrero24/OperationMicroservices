import { Product } from "src/products/entities/product.entity";
import { Column, Entity, OneToMany, PrimaryGeneratedColumn } from "typeorm";

@Entity()
export class Category {
    @PrimaryGeneratedColumn()
    id_categoria: number;
  
    @Column()
    nombre_categoria: string;
  
    @OneToMany(() => Product, (producto) => producto.categoria)
    productos: Product[];
}
