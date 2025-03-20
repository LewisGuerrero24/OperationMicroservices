using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Application.Dtos;
using Domain.Entities;

namespace Domain.Ports
{
    public interface IBranchRepository
    {
         Task<ICollection<Branch>> getAllPayment();

        Task<Branch> BranchFindById(int branch_Id);

        Task<Branch> createBranch(Branch newBranch);

        Task<Branch> updateBranch(Branch branchUpdate, Branch newBranch);

        Task<Branch> deleteBranch(Branch branch);
    }
}