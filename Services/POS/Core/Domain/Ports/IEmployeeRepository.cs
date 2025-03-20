using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Domain.Entities;

namespace Domain.Ports
{
    public interface IEmployeeRepository
    {
        Task<ICollection<Employee>>  GetAllEmployee();

        Task<Employee> EmployeeFindById(int employee_Id);

        Task<Employee> CreateEmployee(Employee newEmployee);

        Task<Employee> UpdateEmployee(Employee newEmployee, Employee employee);

        Task<Employee> DeleteEmployee(Employee employee);
    }
}