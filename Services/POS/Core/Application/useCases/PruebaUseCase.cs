using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Domain.Entities;

namespace Application.useCases
{
    public interface PruebaUseCase
    {
        IEnumerable<Prueba> pruebaLIst();
        String NamePrueba(string name);
    }
}