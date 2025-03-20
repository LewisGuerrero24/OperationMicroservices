using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Domain.Entities;
using Domain.Ports;
using Infrastructure.Data;

namespace Infrastructure.Adapters
{
    public class PruebaRepository : IPruebaRepository
    {
        private readonly MyContext _context;
       
        public PruebaRepository(MyContext context)
        {
            _context = context;
        }

        public IEnumerable<Prueba> getAllUsers()
        {
            var dataPrueba = _context.pruebas.ToList();
            return dataPrueba;
        }

        public string PruebaName(string name)
        {
            string Name = $"{name}";
            return Name;
        }

        
    }
}