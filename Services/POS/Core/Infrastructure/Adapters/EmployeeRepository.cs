using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Domain.Entities;
using Domain.Ports;
using Infrastructure.Data;
using Microsoft.EntityFrameworkCore;

namespace Infrastructure.Adapters
{
    public class EmployeeRepository : IEmployeeRepository
    {
        private readonly MyContext _myContext;

        public EmployeeRepository(MyContext myContext)
        {
            _myContext = myContext;
        }

        public async Task<Employee> CreateEmployee(Employee newEmployee)
        {
            await _myContext.employees.AddAsync(newEmployee);
            await _myContext.SaveChangesAsync();
            return newEmployee;
        }

        public async Task<Employee> DeleteEmployee(Employee employee)
        {
            _myContext.employees.Remove(employee);
            await _myContext.SaveChangesAsync();
            return employee;
        }

        public async Task<Employee> EmployeeFindById(int Employee_Id)
        {
            var employeeData = await _myContext.employees.FirstOrDefaultAsync(x => x.Id == Employee_Id);
            return employeeData;
        }

        public async Task<ICollection<Employee>> GetAllEmployee()
        {
            var listEmployee = await _myContext.employees.AsNoTracking().ToListAsync();
            return listEmployee;
        }

        public async Task<Employee> UpdateEmployee(Employee employeeUpdate, Employee newEmployee)
        {
             if (employeeUpdate != null)
            {
                // Modificar propiedades
                employeeUpdate.Id = employeeUpdate.Id;
                employeeUpdate.name = newEmployee.name;
                employeeUpdate.lastName = newEmployee.lastName;
                employeeUpdate.email = newEmployee.email;
                employeeUpdate.position = newEmployee.position;
                employeeUpdate.phone = newEmployee.phone;
                //branchUpdate.UpdateDate =  DateTime.Today;
                // ... otras propiedades

                await _myContext.SaveChangesAsync();
            }
            return employeeUpdate;
        }
    }
}