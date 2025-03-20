using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Domain.Entities
{
    public class ExpenseReport
    {
        public int ExpenseReportID { get; set; } // Id del informe de gastos

        public int PurchaseOrderID { get; set; } // Id de la orden de compra

        public string ExpenseType { get; set; } // Materia prima, logística, impuestos

        public decimal Amount { get; set; } // Monto del gasto

        public string Status { get; set; } // Pendiente, Aprobado, Rechazado

        public PurchaseOrder PurchaseOrder { get; set; } // Orden de compra

        public bool IsActive { get; set; } // Activo o inactivo

        public DateTime? CreationDate { get; set; }

        public DateTime? ModificationDate { get; set; }
    }
}