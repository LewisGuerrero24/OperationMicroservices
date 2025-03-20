using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Application.Dtos;
using Application.Services;
using Domain.Entities;
using Microsoft.AspNetCore.Mvc;

namespace Api.Controller
{
    [ApiController]
    [Route("api/[controller]")]
    public class BranchController : ControllerBase
    {
        
        private readonly BranchServices _branchServices;

        public BranchController(BranchServices branchServices)
        {
            _branchServices = branchServices;
        }

        [HttpGet]
        public async Task<ActionResult<ICollection<Branch>>> GetBranches(){
            var branches = await _branchServices.getList();
            return Ok(branches);
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<Branch>> GetBranch(int id){
            var branch = await _branchServices.BranchUnique(id);
            if(branch == null){
                return NotFound();
            }
            return Ok(branch);
        }


        [HttpPost]
        public async Task<ActionResult<Branch>> createBranch(BranchDto newBranch){
            var brachCreated = await _branchServices.createBranch(newBranch);
            return Ok(brachCreated);
        }

        [HttpPut("{branch_Id}")]
        public async Task<ActionResult<Branch>> updateBranch(int branch_Id, Branch newBranch){
             if ( branch_Id != newBranch.Id)
            {
                return BadRequest("El ID del producto no coincide.");
            }

            var resultado = await _branchServices.updateBranch(branch_Id, newBranch);

            return Ok(resultado);

        }

        [HttpDelete("{id}")]
        public async Task<ActionResult<Branch>> deleteBranch(int id){
             var resultado = await _branchServices.deleteBranch(id);
            if (resultado == null)
            {
                return NotFound();
            }

            return Ok("Datos Eliminados : "+ resultado);
        }

    }
}