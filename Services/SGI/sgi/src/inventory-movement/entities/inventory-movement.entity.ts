import { Product } from "src/products/entities/product.entity";
import { WareHouse } from "src/ware-house/entities/ware-house.entity";
import { Column, Entity, ManyToOne, PrimaryGeneratedColumn } from "typeorm";

@Entity()
export class InventoryMovement {
  @PrimaryGeneratedColumn()
  id_movimiento: number;

  @ManyToOne(() => Product, (producto) => producto.id_producto)
  producto: Product;

  @ManyToOne(() => WareHouse, (almacen) => almacen.id_almacen)
  almacen: WareHouse;

  @Column()
  tipo_movimiento: string; // Entrada / Salida

  @Column()
  cantidad: number;

  @Column({ type: 'date' })
  fecha_movimiento: Date;

  @Column()
  razon: string; // Compra, venta, ajuste

  @Column()
  realizado_por_user: number;
}
