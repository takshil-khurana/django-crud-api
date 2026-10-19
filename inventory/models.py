# FILE: inventory/models.py

from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

class ProductGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.PROTECT,
        related_name="products",
    )
    group = models.ForeignKey(
        ProductGroup,
        on_delete=models.PROTECT,
        related_name="products",
    )

    def __str__(self) -> str:
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self) -> str:
        return self.name

class PurchaseOrder(models.Model):
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        related_name="purchase_orders",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="purchase_orders",
    )
    quantity = models.PositiveIntegerField()
    order_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"PO-{self.pk}"