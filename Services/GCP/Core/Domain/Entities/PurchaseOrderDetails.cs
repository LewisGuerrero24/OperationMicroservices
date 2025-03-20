using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Domain.Entities
{
    public class PurchaseOrderDetail
    {
        public int PurchaseOrderDetailID { get; set; } // Id del detalle de la orden de compra

        public int PurchaseOrderID { get; set; } // Id de la orden de compra

        public long ProductID { get; set; } // Id del producto

        public int Quantity { get; set; } // Cantidad

        public decimal UnitPrice { get; set; } // Precio unitario

        public DateTime? RequiredDate { get; set; } // Fecha requerida

        public string Status { get; set; } // Pendiente, Aprobado, Rechazado

        public string DestinationWarehouse { get; set; } // Almacén de destino
            
        public PurchaseOrder PurchaseOrder { get; set; } // Orden de compra

        public bool IsActive { get; set; } // Activo o inactivo
        
        public DateTime? CreationDate { get; set; }

        public DateTime? ModificationDate { get; set; }
    }
}