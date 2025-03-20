using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Domain.Entities;

namespace Domain.Ports
{
    public interface ICustomerRepository
    {
        Task<ICollection<Customer>> getAllCustomer();

        Task<Customer> CustomerFindById(int customer_Id);

        Task<Customer> createCustomer(Customer newCustomer);

        Task<Customer> updateCustomer(Customer customerUpdate, Customer newCustomer);

        Task<Customer> deleteCustomer(Customer customer);
    }
}