using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Domain
{
    public record employeeDto( string name ,string lastName ,string position,string phone ,string email ,DateTime hiring_Date);
}