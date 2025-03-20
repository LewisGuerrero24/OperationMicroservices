using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Domain.Entities
{
    public class SupplierPayment
    {
        public int SupplierPaymentID { get; set; } // Id de la factura de pago

        public int PurchaseOrderID { get; set; } // Id de la orden de compra

        public DateTime PaymentDate { get; set; } // Fecha de pago

        public decimal Amount { get; set; } // Monto de la factura

        public string PaymentMethod { get; set; } // Método de pago

        public string PaymentStatus { get; set; } // Pendiente, Pagado, Vencido

        public PurchaseOrder PurchaseOrder { get; set; } // Orden de compra

        public bool IsActive { get; set; } // Activo o inactivo
        
        public DateTime? CreationDate { get; set; }

        public DateTime? ModificationDate { get; set; }
    }
}