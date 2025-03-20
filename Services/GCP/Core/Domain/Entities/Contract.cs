using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Domain.Entities
{
    public class Contract
    {
        public int ContractID { get; set; } // Id del contrato

        public int SupplierID { get; set; } // Id del proveedor

        public DateTime StartDate { get; set; } // Fecha de inicio

        public DateTime EndDate { get; set; } // Fecha de finalización

        public string Terms { get; set; } // Términos del contrato

        public string Status { get; set; } // Pendiente, Activo, Inactivo

        public  Supplier Supplier { get; set; } // Proveedor

        public bool IsActive { get; set; } // Activo o inactivo

        public DateTime? CreationDate { get; set; }

        public DateTime? ModificationDate { get; set; }
    }
}