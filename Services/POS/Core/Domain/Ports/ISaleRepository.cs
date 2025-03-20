using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Domain.Entities;

namespace Domain.Ports
{
    public interface ISaleRepository
    {
        Task<ICollection<Sale>>  getAllSale();

        Task<Sale> SaleFindById(int employee_Id);

        Task<Sale> createSale(Sale saleNew);

        Task<Sale> updateSale(Sale updateSale, Sale sale);

        Task<Sale> deleteSale(Sale sale);
    }
}