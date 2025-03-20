using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;


namespace Domain.Entities
{
    public class Invoice 
    {
        public int InvoiceId { get; set; } // Id de la factura
        
        public int PurchaseOrderID { get; set; }  // Id de la orden de compra

        public int SupplierID { get; set; } // Id del proveedor

        public string InvoiceNumber { get; set; } // Numero de factura

        public DateTime IssueDate { get; set; } // Fecha de emisión

        public DateTime DueDate { get; set; } // Fecha de vencimiento

        public decimal TotalAmount { get; set; } // Total de la factura

        public string Status { get; set; } // Pendiente, Pagada, Vencida

        public bool IsActive { get; set; } // Activo o inactivo

        public PurchaseOrder PurchaseOrder { get; set; }

        public Supplier Supplier { get; set; }

        public DateTime? CreationDate { get; set; }

        public DateTime? ModificationDate { get; set; }
    }
}