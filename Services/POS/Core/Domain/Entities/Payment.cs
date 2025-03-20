
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Domain.Entities
{
       public class Payment: AuditableEntity
    {
       
        public int saleId {get; set;}

        public Sale sale {get; set;} = null!;

        public int typePaymentId {get; set;}

        public typePayment typePayment {get; set;} = null!;

        public int amount {get; set;}

        public DateTime datePayment {get; set;}

    }

}