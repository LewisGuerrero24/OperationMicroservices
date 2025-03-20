using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Domain.Entities
{
    public class GoodsReceipt
    {
        public int GoodsReceiptID { get; set; } // Id de la recibo de productos

        public int PurchaseOrderID { get; set; } // Id de la orden de compra

        public DateTime ReceiptDate { get; set; } // Fecha de entrega

        public long ReceivedBy { get; set; } // Id de la persona que recibe el producto

        public string ReceiptStatus { get; set; } // Pendiente, Recibido, Enviado

        public string Notes { get; set; } // Notas

        public string AttachmentPath { get; set; } // Ruta de la imagen adjunta

        public PurchaseOrder PurchaseOrder { get; set; } // Orden de compra

        public bool IsActive { get; set; } // Activo o inactivo

        public DateTime? CreationDate { get; set; }

        public DateTime? ModificationDate { get; set; }

        public List<GoodsReceiptDetail> GoodsReceiptDetails { get; set; } = new List<GoodsReceiptDetail>();

        public ICollection<Return> Returns { get; set; } = new List<Return>();
    }

}