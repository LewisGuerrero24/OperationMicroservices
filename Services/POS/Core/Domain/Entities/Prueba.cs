using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Domain.Entities
{
    public class Prueba
    {
        public Prueba(int? id, string? name)
        {
            this.id = id;
            this.name = name;
        }

        public int? id { get; set; }

        public string? name {get;set;}

        public string? lastname {get;set;}


    }
}