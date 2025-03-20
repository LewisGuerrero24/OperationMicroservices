using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Application.Services;
using Domain;
using Domain.Dtos;
using Domain.Entities;
using Microsoft.AspNetCore.Mvc;

namespace Api.Controller
{
    [ApiController]
    [Route("api/[controller]")]
    public class EmployeeController : ControllerBase
    {
        private readonly EmployeeServices _employeeServices;

        public EmployeeController(EmployeeServices employeeServices)
        {
            _employeeServices = employeeServices;
        }

        [HttpGet]
    public async Task<ActionResult<ICollection<Employee>>> GetEmployee(){
        var employeeList = await _employeeServices.GetList();
        return Ok(employeeList); 
    }

    [HttpGet("{id}")]
    public async Task<ActionResult<Employee>> UniqueEmployee(int id){
        var employeeData = await _employeeServices.EmployeeUnique(id);
        return Ok(employeeData);
    }
    
    [HttpPost]
    public async Task<ActionResult<Employee>> CreateEmployee(employeeDto employee){
        var employeeData = await _employeeServices.CreateEmployee(employee);
        return Ok(employeeData);
    }


    [HttpPut("{customer_id}")]
    public async Task<ActionResult<Employee>> UpdateEmployee(int employee_id,Employee newEmployee){
          if ( employee_id != newEmployee.Id)
            {
                return BadRequest("El ID del Cliente no coincide.");
            }


        var employee = await _employeeServices.UpdateEmployee(employee_id,newEmployee);
        return employee;
    }


    [HttpDelete("{id}")]
    public async Task<ActionResult<Employee>> DeleteCustomer(int id){
         var dataDelete  = await _employeeServices.DeleteEmployee(id);
         return dataDelete;
    }

    }
}