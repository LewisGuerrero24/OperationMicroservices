using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Application.useCases;
using Domain.Dtos;
using Domain.Entities;
using Domain.Ports;

namespace Application.Services
{
    public class SaleServices :     SaleUseCase
    {
        private readonly ISaleRepository _saleRepository;

        public SaleServices(ISaleRepository saleRepository)
        {
            _saleRepository = saleRepository;
        }

        public async Task<Sale> CreateSale(SalesDto newSale)
        {

            var saleNew = new Sale{
                employeeId = newSale.EmployeeId,
                customerId = newSale.CustomerId,
                branchId = newSale.BranchId,
                typePaymentId = newSale.TypePaymentId,
                date = newSale.Date,
                total = newSale.Total 
            };            
            var saleCreated = await _saleRepository.createSale(saleNew);
            return saleCreated;
        }

        public async Task<Sale> DeleteSale(int sale_Id)
        {
            var saleData = await _saleRepository.SaleFindById(sale_Id);
            var saleDelete = await _saleRepository.deleteSale(saleData);
            return saleData;
        }

        public async Task<ICollection<Sale>> GetList()
        {
            var saleList = await _saleRepository.getAllSale();
            return saleList;
        }

        public async Task<Sale> SaleUnique(int Sale_Id)
        {
          var saleData = await _saleRepository.SaleFindById(Sale_Id);
          return saleData;
        }

        public async Task<Sale> UpdateSale(int sale_Id, Sale newSale)
        {
             var saleData = await _saleRepository.SaleFindById(sale_Id);
             return await _saleRepository.updateSale(saleData, newSale);
        }
    }
}