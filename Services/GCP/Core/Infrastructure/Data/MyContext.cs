using Domain.Entities;
using Microsoft.EntityFrameworkCore;

namespace Infrastructure.Data
{
    public class MyContext : DbContext
    {
         public MyContext(DbContextOptions<MyContext> options): base(options){}

        public DbSet<ApprovalWorkflow> ApprovalWorkflow { get; set; }
        public DbSet<Contract> Contract { get; set; }
        public DbSet<ExpenseReport> ExpenseReport { get; set; }
        public DbSet<GoodsReceiptDetail> GoodsReceiptDetail { get; set; }
        public DbSet<GoodsReceipt> GoodsReceipt { get; set; }
        public DbSet<Invoice> Invoice { get; set; }
        public DbSet<PurchaseOrderDetail> PurchaseOrderDetail { get; set; }
        public DbSet<PurchaseOrder> PurchaseOrder { get; set; }
        public DbSet<PurchaseRequestDetail> PurchaseRequestDetail { get; set; }
        public DbSet<PurchaseRequest> PurchaseRequest { get; set; }
        public DbSet<Return> Return { get; set; }
        public DbSet<SupplierPayment> SupplierPayment { get; set; }
        public DbSet<Supplier> Supplier { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder) 
        {
            // 📌 Relación PurchaseOrder → PurchaseOrderDetail (1:N)
            modelBuilder.Entity<PurchaseOrder>()
                .HasMany(po => po.PurchaseOrderDetails)
                .WithOne(pod => pod.PurchaseOrder)
                .HasForeignKey(pod => pod.PurchaseOrderID);

            // 📌 Relación PurchaseRequest → PurchaseRequestDetail (1:N)
            modelBuilder.Entity<PurchaseRequest>()
                .HasMany(pr => pr.PurchaseRequestDetails)
                .WithOne(prd => prd.PurchaseRequest)
                .HasForeignKey(prd => prd.PurchaseRequestID);

            // 📌 Relación GoodsReceipt → GoodsReceiptDetail (1:N)
            modelBuilder.Entity<GoodsReceipt>()
                .HasMany(gr => gr.GoodsReceiptDetails)
                .WithOne(grd => grd.GoodsReceipt)
                .HasForeignKey(grd => grd.GoodsReceiptID);
            
            // 📌 Relación Invoice → PurchaseOrder (N:1)
            modelBuilder.Entity<Invoice>()
                .HasOne(i => i.PurchaseOrder)
                .WithMany(po => po.Invoices)
                .HasForeignKey(i => i.PurchaseOrderID)
                .OnDelete(DeleteBehavior.NoAction);

            // 📌 Relación Invoice → Supplier (N:1)
            modelBuilder.Entity<Invoice>()
                .HasOne(i => i.Supplier)
                .WithMany(s => s.Invoices)
                .HasForeignKey(i => i.SupplierID)
                .OnDelete(DeleteBehavior.NoAction);

            // 📌 Relación SupplierPayment → PurchaseOrders (N:1)
            modelBuilder.Entity<SupplierPayment>()
                .HasOne(sup => sup.PurchaseOrder)
                .WithMany(po => po.SupplierPayments)
                .HasForeignKey(sup => sup.PurchaseOrderID);

            // 📌 Relación ApprovalWorkflow → PurchaseRequest (N:1)
            modelBuilder.Entity<ApprovalWorkflow>()
                .HasOne(aw => aw.PurchaseRequest)
                .WithMany(po => po.ApprovalWorkflows)
                .HasForeignKey(aw => aw.PurchaseRequestID);

            // 📌 Relación Supplier → Contract (N:1)
            modelBuilder.Entity<Contract>()
                .HasOne(c => c.Supplier)
                .WithMany(sp => sp.Contracts)
                .HasForeignKey(c => c.SupplierID);

            // 📌 Relación ExpenseReport → PurchaseOrder (N:1)
            modelBuilder.Entity<ExpenseReport>()
                .HasOne(er => er.PurchaseOrder)
                .WithMany(po => po.ExpenseReports)
                .HasForeignKey(er => er.PurchaseOrderID);

            // 📌 Relación Return → GoodsReceipt (N:1)
            modelBuilder.Entity<Return>()
                .HasOne(r => r.GoodsReceipt)
                .WithMany(gr => gr.Returns)
                .HasForeignKey(r => r.GoodsReceiptID);
        }
    }
}