
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Domain.Entities;
using Microsoft.EntityFrameworkCore;


namespace Infrastructure.Data
{
    public class MyContext : DbContext
    {
         public MyContext(DbContextOptions<MyContext> options): base(options){
            
            }

        public DbSet<Prueba> pruebas {get; set;}

        public DbSet<Sale> sales { get; set; }

          public DbSet<SalesDetail> salesDetails { get; set; }

        public DbSet<Branch> branches {get; set;}

        public DbSet<Customer> customers {get; set;}

        public DbSet<Employee> employees { get; set; }

        public DbSet<Payment> payments { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Branch>()
            .HasMany(e => e.sales)
            .WithOne(e => e.branch)
            .HasForeignKey(e => e.branchId)
            .IsRequired();

             modelBuilder.Entity<Customer>()
            .HasMany(e => e.sales)
            .WithOne(e => e.customer)
            .HasForeignKey(e => e.customerId)
            .IsRequired();
        

             modelBuilder.Entity<Employee>()
            .HasMany(e => e.sales)
            .WithOne(e => e.employee)
            .HasForeignKey(e => e.employeeId)
            .IsRequired();

            modelBuilder.Entity<typePayment>()
            .HasMany(e => e.sales)
            .WithOne(e => e.typePayment)
            .HasForeignKey(e => e.typePaymentId)
            .OnDelete(DeleteBehavior.NoAction) // Cambiado a Restrict
            .IsRequired();

            modelBuilder.Entity<typePayment>()
            .HasMany(e => e.payments)
            .WithOne(e => e.typePayment)
            .HasForeignKey(e => e.typePaymentId)
            .OnDelete(DeleteBehavior.NoAction) // Cambiado a Restrict
            .IsRequired();

            modelBuilder.Entity<Sale>()
            .HasMany(e => e.salesDetails)
            .WithOne(e => e.sales)
            .HasForeignKey(e => e.salesId)
            .IsRequired();
        }

    

    }

}