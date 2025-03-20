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
    public class BranchRepository : IBranchRepository
    {
        private readonly MyContext _myContext;

        public BranchRepository(MyContext myContext)
        {
            _myContext = myContext;
        }

        public async Task<Branch> BranchFindById(int branch_Id)
        {
            var branchData = await _myContext.branches.FirstOrDefaultAsync(x => x.Id == branch_Id);
            return branchData;
        }

        public async Task<Branch> createBranch(Branch newBranch)
        {
            _myContext.branches.Add(newBranch);
            await _myContext.SaveChangesAsync();
            return newBranch;
        }

        public async Task<Branch> deleteBranch(Branch branch)
        {
            _myContext.branches.Remove(branch);
            await _myContext.SaveChangesAsync();
            return branch;
        }

        public async Task<ICollection<Branch>> getAllPayment()
        {
            return await _myContext.branches.ToListAsync();
        }

        public async Task<Branch> updateBranch(Branch branchUpdate, Branch newBranch)
        {
            if (branchUpdate != null)
            {
                // Modificar propiedades
                branchUpdate.Id = branchUpdate.Id;
                branchUpdate.name = newBranch.name;
                branchUpdate.city = newBranch.city;
                branchUpdate.address = newBranch.address;
                //branchUpdate.UpdateDate =  DateTime.Today;
                // ... otras propiedades

                await _myContext.SaveChangesAsync();
            }
            return branchUpdate;
        }
    }
}