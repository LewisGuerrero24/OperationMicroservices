using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Domain.Entities;

namespace Domain.Ports
{
    public interface ISaleDetailRepository
    {
         Task<ICollection<SalesDetail>>  GetAllSalesDetails();

        Task<SalesDetail> SalesDetailsFindById(int details_Id);

        Task<SalesDetail> CreateSalesDetails(SalesDetail newSalesDetail);

        Task<SalesDetail> UpdateSalesDetails(SalesDetail updateSales, SalesDetail newSalesDetail);

        Task<SalesDetail> DeleteSalesDetails(SalesDetail SalesDetail); 
    }
}