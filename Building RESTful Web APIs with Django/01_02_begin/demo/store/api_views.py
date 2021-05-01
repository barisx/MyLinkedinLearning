from rest_framework.generics import ListAPIView

from store.serializers import ProductSerializer
from store.models import Product

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializers_class = ProductSerializer
    