using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Domain.Entities;

namespace Domain.Ports
{
    public interface IPaymentRepository
    {
        ICollection<Payment> getAllPayment();

        Employee PaymentFindById(int payment_Id);

        Employee createPayment(Payment newPayment);

        Employee updatePayment(int payment_Id, Payment payment);

        bool deletePayment(int payment_Id);
    }
}