using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Domain.Entities
{
    public class ApprovalWorkflow
    {
        public int ApprovalWorkflowID { get; set; } // Id de la aprobación de la solicitud de compra

        public int PurchaseRequestID { get; set; } // Id de la solicitud de compra

        public long ApprovedBy { get; set; } // usuario que la aprueba

        public string Status { get; set; } // Pendiente, Aprobado, Rechazado

        public DateTime ApprovalDate { get; set; } // Fecha de aprobación

        public string Comments { get; set; } // Comentarios de la aprobación

        public PurchaseRequest PurchaseRequest { get; set; }

        public bool IsActive { get; set; } // Activo o inactivo

        public DateTime? CreationDate { get; set; }

        public DateTime? ModificationDate { get; set; }
    }
}

