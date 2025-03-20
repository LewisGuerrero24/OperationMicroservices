using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Application.Dtos;
using Domain.Entities;

namespace Application.useCases
{
    public interface BranchUseCase
    {
        Task<ICollection<Branch>> getList();

        Task<Branch> BranchUnique(int branch_Id);

        Task<Branch> createBranch(BranchDto newBranch);

        Task<Branch> updateBranch(int branch_Id, Branch newBranch);

        Task<Branch> deleteBranch(int branch_Id);
    }
}