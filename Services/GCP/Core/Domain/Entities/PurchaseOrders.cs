using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Domain.Entities
{
    public class PurchaseOrder 
    {
        public int PurchaseOrderID { get; set; } // Id de la orden de compra
        
        public int SupplierID { get; set; } // Id del proveedor 

        public DateTime? EstimatedDeliveryDate { get; set; } // Fecha de entrega estimada
        
        public DateTime? ActualDeliveryDate { get; set; } // Fecha de entrega real
        
        public string PaymentTerms { get; set; } // Términos de pago
        
        public string Currency { get; set; } // Divisa o moneda
        
        public decimal Discount { get; set; } // Descuento

        public decimal TotalAmount { get; set; } // Total del pedido valor
        
        public string Notes { get; set; } // Notas
        
        public string Status { get; set; } // Pendiente, Aprobado, Rechazado

        public DateTime? CreationDate { get; set; }

        public DateTime? ModificationDate { get; set; }

        public bool IsActive { get; set; } // Activo o inactivo

        public List<PurchaseOrderDetail> PurchaseOrderDetails { get; set; } = new List<PurchaseOrderDetail>();

        public List<Invoice> Invoices { get; set; } = new List<Invoice>();

        public List<SupplierPayment> SupplierPayments { get; set; } = new List<SupplierPayment>();

        public List<ExpenseReport> ExpenseReports { get; set; } = new List<ExpenseReport>();

        public Supplier Supplier { get; set; }

    }
}