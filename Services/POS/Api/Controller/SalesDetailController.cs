using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Application.Services;
using Domain.Dtos;
using Domain.Entities;
using Microsoft.AspNetCore.Mvc;

namespace Api.Controller
{
    [ApiController]
    [Route("api/[controller]")]
    public class SalesDetailController : ControllerBase
    {
        private readonly SaleDetailsServices _saleDetailsServices;

        public SalesDetailController(SaleDetailsServices saleDetailsServices)
        {
            _saleDetailsServices = saleDetailsServices;
        }

     [HttpGet]
    public async Task<ActionResult<ICollection<SalesDetail>>> GetSalesDetails(){
        var saleDetailList = await _saleDetailsServices.GetList();
        return Ok(saleDetailList); 
    }

    [HttpGet("{id}")]
    public async Task<ActionResult<SalesDetail>> UniqueSalesDetail(int id){
        var saleDetailData = await _saleDetailsServices.SalesDetailUnique(id);
        return Ok(saleDetailData);
    }

    [HttpPost]
    public async Task<ActionResult<Employee>> CreateSalesDetail(SalesDetailsDto salesDetails){
        var salesDetailData = await _saleDetailsServices.CreateSalesDetail(salesDetails);
        return Ok(salesDetailData);
    }


    [HttpPut("{salesDetail_id}")]
    public async Task<ActionResult<SalesDetail>> UpdateSalesDetail(int salesDetail_id,SalesDetail newSalesDetail){
          if ( salesDetail_id != newSalesDetail.Id)
            {
                return BadRequest("El ID del detalle de la venta no coincide.");
            }


        var salesDetail = await _saleDetailsServices.UpdateSalesDetail(salesDetail_id,newSalesDetail);
        return salesDetail;
    }


    [HttpDelete("{id}")]
    public async Task<ActionResult<SalesDetail>> DeleteSalesDetail(int id){
         var dataDelete  = await _saleDetailsServices.DeleteSalesDetail(id);
         return dataDelete;
    }
    }
}