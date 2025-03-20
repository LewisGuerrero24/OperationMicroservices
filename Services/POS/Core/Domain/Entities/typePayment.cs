using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Domain.Entities
{
    public class typePayment : AuditableEntity
    {
        public string name { get; set; }
        public ICollection<Sale> sales {get; set;}

        public ICollection<Payment> payments {get; set;}

    }
}