using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Application.Dtos;
using Application.useCases;
using Domain.Entities;
using Domain.Ports;

namespace Application.Services
{
    public class CustomerServices : CustomerUseCase
    {

        private readonly ICustomerRepository _customerRepository;

        public CustomerServices(ICustomerRepository customerRepository)
        {
            _customerRepository = customerRepository;
        }

        public async Task<Customer> createCustomer(CustomerDto dto)
        {
            var newCustomer = new Customer{
                name = dto.Name,
                lastName = dto.LastName,
                phone = dto.Address,
                email = dto.Email,
                address = dto.Address
            };
            var customer = await _customerRepository.createCustomer(newCustomer);

            return customer;
        }

        public async Task<Customer> CustomerUnique(int customer_Id)
        {
            var customerData = await _customerRepository.CustomerFindById(customer_Id);
            return customerData;
        }

        public async Task<Customer> deleteCustomer(int customer_Id)
        {
            var customerData = await _customerRepository.CustomerFindById(customer_Id);

            var dataDelete = await _customerRepository.deleteCustomer(customerData);

            return dataDelete;
        }

        public async Task<ICollection<Customer>> getList()
        {
            var customerList = await _customerRepository.getAllCustomer();
            return customerList;
        }

        public async Task<Customer> updateCustomer(int customer_Id, Customer newCustomer)
        {
            var customerData = await _customerRepository.CustomerFindById(customer_Id);
             return await _customerRepository.updateCustomer(customerData, newCustomer);
        }
    }
}