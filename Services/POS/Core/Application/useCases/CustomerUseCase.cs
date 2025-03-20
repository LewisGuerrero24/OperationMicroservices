using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Application.Dtos;
using Domain.Entities;

namespace Application.useCases
{
    public interface CustomerUseCase
    {
        Task<ICollection<Customer>> getList();

        Task<Customer> CustomerUnique(int customer_Id);

        Task<Customer> createCustomer(CustomerDto newCustomer);

        Task<Customer> updateCustomer(int customer_Id,Customer newCustomer);

        Task<Customer> deleteCustomer(int customer_Id);
    }
}