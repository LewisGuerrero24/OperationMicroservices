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
    public class SaleDetailRepository : ISaleDetailRepository
    {
        private MyContext _myContext;

        public SaleDetailRepository(MyContext myContext)
        {
            _myContext = myContext;
        }

        public async Task<SalesDetail> CreateSalesDetails(SalesDetail newSalesDetails)
        {
            await _myContext.salesDetails.AddAsync(newSalesDetails);
            await _myContext.SaveChangesAsync();
            return newSalesDetails;
        }

        public async Task<SalesDetail> DeleteSalesDetails(SalesDetail salesDetail)
        {
            _myContext.salesDetails.Remove(salesDetail);
            await _myContext.SaveChangesAsync();
            return salesDetail;
        }

        public async Task<ICollection<SalesDetail>> GetAllSalesDetails()
        {
            var saleDetailData = await _myContext.salesDetails.AsNoTracking().ToListAsync();
            return saleDetailData;
        }

        public async Task<SalesDetail> SalesDetailsFindById(int salesDetail_Id)
        {
            var saleDetailData = await _myContext.salesDetails.FirstOrDefaultAsync(x => x.Id == salesDetail_Id);
            return saleDetailData;
        }

        public async Task<SalesDetail> UpdateSalesDetails(SalesDetail salesDetailUpdate, SalesDetail newSalesDetails)
        {
            if (salesDetailUpdate != null)
            {
                // Modificar propiedades
                salesDetailUpdate.Id = newSalesDetails.Id;
                salesDetailUpdate.product = newSalesDetails.product;
                salesDetailUpdate.quantity = newSalesDetails.quantity;
                salesDetailUpdate.unitPrice = newSalesDetails.unitPrice;
                salesDetailUpdate.subtotal = newSalesDetails.quantity*newSalesDetails.unitPrice;
                //branchUpdate.UpdateDate =  DateTime.Today;
                // ... otras propiedades

                await _myContext.SaveChangesAsync();
            }
            return salesDetailUpdate;
        }
    }
}