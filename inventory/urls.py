from rest_framework.routers import DefaultRouter
from .views import (
    ProductCategoryViewSet,
    ProductGroupViewSet,
    ProductViewSet,
    SupplierViewSet,
    PurchaseOrderViewSet,
)

router = DefaultRouter()

router.register(
    "categories",
    ProductCategoryViewSet,
    basename="category",
)
router.register(
    "product-groups",
    ProductGroupViewSet,
    basename="product-group",
)
router.register(
    "products",
    ProductViewSet,
    basename="product",
)
router.register(
    "suppliers",
    SupplierViewSet,
    basename="supplier",
)
router.register(
    "purchase-orders",
    PurchaseOrderViewSet,
    basename="purchase-order",
)

urlpatterns = router.urls