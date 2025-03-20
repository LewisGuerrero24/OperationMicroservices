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
    public class BranchServices : BranchUseCase
    {   
        private readonly IBranchRepository _branchRepository;

        public BranchServices(IBranchRepository branchRepository)
        {
            _branchRepository = branchRepository;
        }

        public async Task<Branch> BranchUnique(int branch_Id)
        {
            Branch branchData = await _branchRepository.BranchFindById(branch_Id);
            return branchData;
        }

        public async Task<Branch> createBranch(BranchDto BranchDto)
        {

            var newBranch = new Branch{
                name = BranchDto.Name,
                city = BranchDto.City,
                phone = BranchDto.Phone,
                address = BranchDto.Address
            };
            Branch newBranchData = await _branchRepository.createBranch(newBranch);
            return newBranchData;
        }

        public async Task<Branch> deleteBranch(int branch_Id)
        {
            var dataBranchDelete =await _branchRepository.BranchFindById(branch_Id);
            Branch branchData =  await _branchRepository.deleteBranch(dataBranchDelete);
            return branchData;
        }

        public Task<ICollection<Branch>> getList()
        {
            var listBranch = _branchRepository.getAllPayment();
            return listBranch;
        }

        public async Task<Branch> updateBranch(int branch_Id,Branch newbranch)
        {
            var dataBranchUpdate = await _branchRepository.BranchFindById(branch_Id);
            
            return await _branchRepository.updateBranch(dataBranchUpdate, newbranch);
        }

        
    }
}