using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Domain.Entities;
using Domain.Ports;
using Infrastructure.Data;
using Microsoft.EntityFrameworkCore;

namespace Infrastructure.Adapters
{
    public class SaleRepository : ISaleRepository
    {
        private readonly MyContext _myContext;

        public SaleRepository(MyContext myContext)
        {
            _myContext = myContext;
        }

        public async Task<Sale> createSale(Sale newSale)
        {
            await _myContext.sales.AddAsync(newSale);
            await _myContext.SaveChangesAsync();
            return newSale;
        }

        public async Task<Sale> deleteSale(Sale newSale)
        {
            _myContext.sales.Remove(newSale);
            await _myContext.SaveChangesAsync();
            return newSale;
        }

        public async Task<ICollection<Sale>> getAllSale()
        {
             var listSale = await _myContext.sales.AsNoTracking().ToListAsync();
            return listSale;
        }

        public async Task<Sale> SaleFindById(int sale_Id)
        {
            var saleData = await _myContext.sales.FirstOrDefaultAsync(x => x.Id == sale_Id);
            return saleData;
        }

        public async Task<Sale> updateSale(Sale saleUpdate, Sale sale)
        {
             if (saleUpdate != null)
            {
                // Modificar propiedades
                saleUpdate.Id = saleUpdate.Id;
                saleUpdate.branchId = sale.branchId;
                saleUpdate.customerId = sale.customerId;
                saleUpdate.employeeId = sale.employeeId;
                saleUpdate.date = sale.date;
                saleUpdate.total = sale.total;
                //branchUpdate.UpdateDate =  DateTime.Today;
                // ... otras propiedades

                await _myContext.SaveChangesAsync();
            }
            return saleUpdate;
        }
    }
}