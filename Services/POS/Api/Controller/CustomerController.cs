using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Application.Dtos;
using Application.Services;
using Domain.Entities;
using Microsoft.AspNetCore.Mvc;

namespace Api.Controller
{
    [ApiController]
    [Route("api/[controller]")]
    public class CustomerController : ControllerBase
    {
        private readonly CustomerServices _customerServices;

        public CustomerController(CustomerServices customerServices)
        {
            _customerServices = customerServices;
        }

    [HttpGet]
    public async Task<ActionResult<ICollection<Customer>>> GetCustomers(){
        var customerList = await _customerServices.getList();
        return Ok(customerList); 
    }

    [HttpGet("{id}")]
    public async Task<ActionResult<Customer>> UniqueCustomer(int id){
        var customerData = await _customerServices.CustomerUnique(id);
        return Ok(customerData);
    }

    [HttpPost]
    public async Task<ActionResult<Customer>> CreateCustomer(CustomerDto customer){
        var customerData = await _customerServices.createCustomer(customer);
        return Ok(customerData);
    }


    [HttpPut("{customer_id}")]
    public async Task<ActionResult<Customer>> UpdateCustomer(int customer_id,Customer newCustomer){
          if ( customer_id != newCustomer.Id)
            {
                return BadRequest("El ID del Cliente no coincide.");
            }


        var customer = await _customerServices.updateCustomer(customer_id,newCustomer);
        return customer;
    }


    [HttpDelete("{id}")]
    public async Task<ActionResult<Customer>> DeleteCustomer(int id){
         var dataDelete  = await _customerServices.deleteCustomer(id);
         return dataDelete;
    }

    }
}