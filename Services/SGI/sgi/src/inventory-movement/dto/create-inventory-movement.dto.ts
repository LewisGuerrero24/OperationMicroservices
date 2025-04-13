import { ApiProperty } from "@nestjs/swagger";

export class CreateInventoryMovementDto {
    
      @ApiProperty({example:0, description: "Id_Producto",required: true})  
      producto: number;
    
      @ApiProperty({example:0, description: "Id_Almacen",required: true})  
      almacen: number;
    
      @ApiProperty({example:"ENTRADA/SALIDA", description: "tipo_movimiento",required: true})  
      tipo_movimiento: string; // Entrada / Salida
    
      @ApiProperty({example:0, description: "cantidad_unidades_ajuste",required: true})  
      cantidad: number;
    
      @ApiProperty({example:"COMPRA/VENTA/AJUSTE", description: "razon_ajuste", required:true})
      razon: string; // Compra, venta, ajuste
    
      @ApiProperty({example:0,description: "Usuario_Movimiento", required:true})
      realizado_por_user: number;
}
