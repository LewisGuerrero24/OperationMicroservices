using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Domain.Entities
{
    public class PurchaseRequest
    {
        public int PurchaseRequestID { get; set; } // Id de la solicitud de compra

        public DateTime RequestDate { get; set; } // Fecha de la solicitud de compra

        public long RequestedBy { get; set; } // Usuario que realizo la solicitud de compra

        public string Status { get; set; } // Pendiente, Aprobado, Rechazado

        public string Comments { get; set; } // Comentarios de la solicitud de compra
        
        public DateTime? CreationDate { get; set; } 

        public DateTime? ModificationDate { get; set; }

        public bool IsActive { get; set; } // Activo o inactivo

        public List<PurchaseRequestDetail> PurchaseRequestDetails { get; set; } = new List<PurchaseRequestDetail>();

        public List<ApprovalWorkflow> ApprovalWorkflows { get; set; } = new List<ApprovalWorkflow>();
    }
}