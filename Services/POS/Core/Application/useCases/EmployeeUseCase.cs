using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Domain;
using Domain.Entities;

namespace Application.useCases
{
    public interface EmployeeUseCase
    {
        Task<ICollection<Employee>> GetList();

        Task<Employee> EmployeeUnique(int customer_Id);

        Task<Employee> CreateEmployee(employeeDto newEmployee);

        Task<Employee> UpdateEmployee(int employee_Id,Employee newEmployee);

        Task<Employee> DeleteCustomer(int employee_Id); 
    }
}