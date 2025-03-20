using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Domain.Entities
{
    public class PurchaseRequestDetail
    {
        public int PurchaseRequestDetailID { get; set; } // Id del detalle de la solicitud de compra
 
        public int PurchaseRequestID { get; set; } // Id de la solicitud de compra

        public long ProductID { get; set; } // Id del producto

        public int Quantity { get; set; } // Cantidad de productos

        public DateTime? NeededByDate { get; set; } // Fecha de la necesidad de productos

        public PurchaseRequest PurchaseRequest { get; set; } // Solicitud de compra

        public bool IsActive { get; set; } // Activo o inactivo

        public DateTime? CreationDate { get; set; } 

        public DateTime? ModificationDate { get; set; }
        
    }
}