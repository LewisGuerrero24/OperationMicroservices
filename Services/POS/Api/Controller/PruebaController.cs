using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Application.Services;
using Domain.Entities;
using Infrastructure.Data;
using Microsoft.AspNetCore.Mvc;

namespace Api.Controller
{
    [ApiController]
    [Route("api/[controller]")]
    public class PruebaController : ControllerBase
    {
        private readonly PruebaService _pruebaService;

        public PruebaController(PruebaService pruebaService)
        {
            _pruebaService = pruebaService;
        }

        [HttpGet]
        public ActionResult<string> getName()
        {
            return Ok(_pruebaService.NamePrueba("Lewis Guerrero"));
        }

        [HttpGet("list")]
        public ActionResult<IEnumerable<Prueba>> getAllPruebas()
        {
            return Ok(_pruebaService.pruebaLIst());
        }
    }
}