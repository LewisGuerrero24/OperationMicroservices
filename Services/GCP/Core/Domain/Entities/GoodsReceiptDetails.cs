using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Domain.Entities
{
    public class GoodsReceiptDetail
    {
        public int GoodsReceiptDetailID { get; set; } // Id del detalle de la recibo de productos

        public int GoodsReceiptID { get; set; }  // Id de la recibo de productos

        public int ProductID { get; set; } // Id del producto

        public string Quality { get; set; } // Calidad

        public string WarehouseLocation { get; set; } // Almacén

        public string Discrepancies { get; set; } // Discrepancias

        public GoodsReceipt GoodsReceipt { get; set; } // Recibo de productos

        public bool IsActive { get; set; } // Activo o inactivo

        public DateTime? CreationDate { get; set; }

        public DateTime? ModificationDate { get; set; }
    }
}