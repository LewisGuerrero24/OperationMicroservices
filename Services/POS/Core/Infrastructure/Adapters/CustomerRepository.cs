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
    public class CustomerRepository : ICustomerRepository
    {

        private readonly MyContext _myContext;

        public CustomerRepository(MyContext myContext)
        {
            _myContext = myContext;
        }

        public async Task<Customer> createCustomer(Customer newCustomer)
        {
            await _myContext.customers.AddAsync(newCustomer);
            await _myContext.SaveChangesAsync();
            return newCustomer;
        }

        public async Task<Customer> CustomerFindById(int customer_Id)
        {
            var customerData = await _myContext.customers.FirstOrDefaultAsync(x => x.Id == customer_Id);
            return customerData;
        }

        public async Task<Customer> deleteCustomer(Customer customer)
        {
            _myContext.customers.Remove(customer);
            await _myContext.SaveChangesAsync();
            return customer;
        }

        public async Task<ICollection<Customer>> getAllCustomer()
        {
            var listCustoer = await _myContext.customers.AsNoTracking().ToListAsync();
            return listCustoer;
        }

        public async Task<Customer> updateCustomer(Customer customerUpdate, Customer newCustomer)
        {
             if (customerUpdate != null)
            {
                // Modificar propiedades
                customerUpdate.Id = customerUpdate.Id;
                customerUpdate.name = newCustomer.name;
                customerUpdate.lastName = newCustomer.lastName;
                customerUpdate.email = newCustomer.email;
                customerUpdate.address = newCustomer.address;
                customerUpdate.phone = newCustomer.phone;
                //branchUpdate.UpdateDate =  DateTime.Today;
                // ... otras propiedades

                await _myContext.SaveChangesAsync();
            }
            return customerUpdate;
        }
    }
}