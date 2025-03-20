using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Domain.Entities;

namespace Domain.Ports
{
    public interface IPruebaRepository
    {
        String PruebaName(string name);
        IEnumerable<Prueba> getAllUsers();
    }
}