using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Application.useCases;
using Domain.Entities;
using Domain.Ports;


namespace Application.Services
{
    public class PruebaService : PruebaUseCase
    {   
        private readonly IPruebaRepository _pruebaRepository;

        public PruebaService(IPruebaRepository pruebaRepository)
        {
            _pruebaRepository = pruebaRepository;
        }

        public string NamePrueba(string name)
        {
            return _pruebaRepository.PruebaName(name);
        }

        public IEnumerable<Prueba> pruebaLIst()
        {
            return _pruebaRepository.getAllUsers();
        }
    }
}