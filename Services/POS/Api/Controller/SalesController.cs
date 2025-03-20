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
    public class SalesController : ControllerBase
    {
        private readonly SaleServices _saleServices;

        public SalesController(SaleServices saleServices)
        {
            _saleServices = saleServices;
        }

            [HttpGet]
    public async Task<ActionResult<ICollection<Sale>>> GetSale(){
        var saleList = await _saleServices.GetList();
        return Ok(saleList); 
    }

    [HttpGet("{id}")]
    public async Task<ActionResult<Sale>> UniqueSale(int id){
        var saleData = await _saleServices.SaleUnique(id);
        return Ok(saleData);
    }

    [HttpPost]
    public async Task<ActionResult<Sale>> CreateSale(SalesDto sale){
        var saleData = await _saleServices.CreateSale(sale);
        return Ok(saleData);
    }


    [HttpPut("{sale_id}")]
    public async Task<ActionResult<Sale>> UpdateSale(int sale_id,Sale newSale){
          if ( sale_id != newSale.Id)
            {
                return BadRequest("El ID del Cliente no coincide.");
            }


        var sale = await _saleServices.UpdateSale(sale_id,newSale);
        return sale;
    }


    [HttpDelete("{id}")]
    public async Task<ActionResult<Sale>> DeleteSale(int id){
         var dataDelete  = await _saleServices.DeleteSale(id);
         return dataDelete;
    }
    }
}