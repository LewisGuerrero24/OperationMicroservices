using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Domain.Entities
{
    public class SalePayment : AuditableEntity
    {
        public int SaleId { get; set; }
        public Sale Sale { get; set; } = null!;

        public int PaymentId { get; set; }
        public Payment Payment { get; set; } = null!;

        public DateTime LinkedAt { get; set; }
    }
}