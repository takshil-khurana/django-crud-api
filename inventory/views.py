from django.http import JsonResponse
from.models import Product
def product_list(request):
    products = Product.objects.all()
    data = [{'id': product.id, 'name': product.name, 'description': product.description, 'price': str(product.price), 'quantity': product.quantity} for product in products]
    return JsonResponse(data, safe=False)
# Create your views here.
