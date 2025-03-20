
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Domain.Entities
{
    public class Branch : AuditableEntity
    {
        public string name { get; set; }

        public string city { get; set; }

        public string address {get; set;}

        public string phone {get; set;}

        public ICollection<Sale> sales { get; set; } = new List<Sale>();
}}

