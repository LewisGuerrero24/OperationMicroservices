using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Domain.Entities
{
    public class Return 
    {
        public int ReturnID { get; set; } // Id del retorno o devolución de compra

        public int GoodsReceiptID { get; set; } // Id del recibo de productos

        public int ProductID { get; set; } // Id del producto

        public int ReturnedQuantity { get; set; } // Cantidad devuelta

        public string Reason { get; set; } // Razón del retorno o devolución

        public string Status { get; set; } // Pendiente, Aprobada, Rechazada

        public bool IsActive { get; set; } // Activo o inactivo

        public GoodsReceipt GoodsReceipt { get; set; }

        public DateTime? CreationDate { get; set; }

        public DateTime? ModificationDate { get; set; }

    }
}