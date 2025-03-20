using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Application.useCases;
using Domain.Dtos;
using Domain.Entities;
using Domain.Ports;

namespace Application.Services{
public class SaleDetailsServices : SalesDetailUseCase
    { 
        private readonly ISaleDetailRepository _saleDetailRepository;

        public SaleDetailsServices(ISaleDetailRepository saleDetailRepository)
        {
            _saleDetailRepository = saleDetailRepository;
        }

        public async Task<SalesDetail> CreateSalesDetail(SalesDetailsDto salesDetailsDto)
        {
            var newSalesDetails = new SalesDetail{
                product = salesDetailsDto.Product,
                quantity = salesDetailsDto.Quantity,
                unitPrice = salesDetailsDto.UnitPrice,
                subtotal = salesDetailsDto.Quantity*salesDetailsDto.UnitPrice 

            };
            var SalesDetailCreate = await _saleDetailRepository.CreateSalesDetails(newSalesDetails);

            return SalesDetailCreate;
        }

        public async Task<SalesDetail> DeleteSalesDetail(int salesDetail_Id)
        {
            var saleDetailDelete = await _saleDetailRepository.SalesDetailsFindById(salesDetail_Id);
            var saleDetailData = await _saleDetailRepository.DeleteSalesDetails(saleDetailDelete);
            return saleDetailData; 
        }

        public async Task<ICollection<SalesDetail>> GetList()
        {
            var ListData = await _saleDetailRepository.GetAllSalesDetails();
            return ListData;
        }
 
        public async Task<SalesDetail> SalesDetailUnique(int SalesDetail_Id)
        {
            var saleDetail = await _saleDetailRepository.SalesDetailsFindById(SalesDetail_Id);
            return saleDetail;
        }

        public async Task<SalesDetail> UpdateSalesDetail(int saleDetail_Id, SalesDetail newSalesDetail)
        
        {
            var saleDetail = await _saleDetailRepository.SalesDetailsFindById(saleDetail_Id);
            var saleDetailUpdate = await _saleDetailRepository.UpdateSalesDetails(saleDetail,newSalesDetail);
            return saleDetailUpdate;
        }
    }
}