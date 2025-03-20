using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Domain.Entities
{
    public class Supplier
    {
        public int SupplierID { get; set; } // Id del Proveedor

        public string Name { get; set; } // Nombre del proveedor

        public string ContactPerson { get; set; } // Persona de contacto

        public string Phone { get; set; } // Teléfono

        public string Email { get; set; } // Correo electrónico

        public string Address { get; set; } // Dirección

        public string PaymentTerms { get; set; } // Términos de pago

        public string BankDetails { get; set; } // Detalles de la cuenta bancaria

        public bool Active { get; set; } // Activo o inactivo

        public DateTime? CreationDate { get; set; } 

        public bool IsActive { get; set; } // Activo o inactivo

        public DateTime? ModificationDate { get; set; }

        public List<Invoice> Invoices { get; set; } = new List<Invoice>();

        public List<Contract> Contracts { get; set; } = new List<Contract>();
    }
}