from rest_framework.viewsets import ModelViewSet
from .models import (
    ProductCategory,
    ProductGroup,
    Product,
    Supplier,
    PurchaseOrder,
)
from .serializers import (
    ProductCategorySerializer,
    ProductGroupSerializer,
    ProductSerializer,
    SupplierSerializer,
    PurchaseOrderSerializer,
)

class ProductCategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ProductGroupViewSet(ModelViewSet):
    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related(
        "category", "group"
    ).all()
    serializer_class = ProductSerializer

class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class PurchaseOrderViewSet(ModelViewSet):
    queryset = PurchaseOrder.objects.select_related(
        "supplier", "product"
    ).all()
    serializer_class = PurchaseOrderSerializer