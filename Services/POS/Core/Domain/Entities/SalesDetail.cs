using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Domain.Entities
{
    public class SalesDetail : AuditableEntity
    {
        public int salesId { get; set; }

        public Sale sales {get; set;} = null!;

        public int product {get; set;}

        public int quantity {get; set;}

        public int unitPrice {get; set;}

        public int subtotal {get; set;}




    }
}