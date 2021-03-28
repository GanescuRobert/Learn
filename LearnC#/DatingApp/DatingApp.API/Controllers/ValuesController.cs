using System.Collections.Generic;
using System.Linq;
using DatingApp.API.Data;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace DatingApp.API.Controllers
{
    //
    [Route("api/[controller]")]
    [ApiController]
    public class ValuesController : ControllerBase
    {
        private readonly DataContext _context;
        public ValuesController(DataContext context)
        {
            _context = context;
        }
        //Get api/values
        [HttpGet]
        public async System.Threading.Tasks.Task<IActionResult> GetValuesAsync()
        {
            var values = await _context.Values.ToListAsync();
            return Ok(values);
        }
        [HttpGet("{id}")]
        public async System.Threading.Tasks.Task<IActionResult> GetValueAsync(int id)
        {
            var value = await _context.Values.FirstOrDefaultAsync(x => x.Id == id);
            return Ok(value);
        }
    }
}
