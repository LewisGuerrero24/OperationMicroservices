using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Application.useCases;
using Domain;
using Domain.Entities;
using Domain.Ports;

namespace Application.Services
{
    public class EmployeeServices : EmployeeUseCase
    {

        private readonly IEmployeeRepository _employeeRepository;

        public EmployeeServices(IEmployeeRepository employeeRepository)
        {
            _employeeRepository = employeeRepository;
        }

        public async Task<Employee> CreateEmployee(employeeDto employeeDto)
        {
            var newEmployee = new Employee{
                name = employeeDto.name,
                lastName = employeeDto.lastName,
                phone = employeeDto.phone,
                position = employeeDto.position,
                email = employeeDto.email
            };

            var dataEmployee = await _employeeRepository.CreateEmployee(newEmployee);
            return dataEmployee;

        }

        public Task<Employee> DeleteCustomer(int employee_Id)
        {
            throw new NotImplementedException();
        }

        public async Task<Employee> DeleteEmployee(int employee_Id)
        {
            var employeeDelete = await _employeeRepository.EmployeeFindById(employee_Id);
            var employeeData = await _employeeRepository.DeleteEmployee(employeeDelete);
            return employeeData; 
        }

        public async Task<Employee> EmployeeUnique(int Employee_Id)
        {
            var employeeData = await _employeeRepository.EmployeeFindById(Employee_Id);
            return employeeData;
        }

        public async Task<ICollection<Employee>> GetList()
        {
            var listEmployee = await _employeeRepository.GetAllEmployee();
            return listEmployee;
        }

        public async Task<Employee> UpdateEmployee(int employee_Id, Employee newEmployee)
        {
             var employeeData = await _employeeRepository.EmployeeFindById(employee_Id);
             return await _employeeRepository.UpdateEmployee(employeeData, newEmployee);
        }
    }
}