using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Domain.Dtos
{
    public record SalesDetailsDto(int Product,int Quantity ,int UnitPrice ,int Subtotal );
}