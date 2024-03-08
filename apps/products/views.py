from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from apps.products.models import Product
from apps.products.serializers import ProductSerializer

# Create your views here.
class ProductListAPI(ListAPIView): #GET
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class ProductCreateAPIView(CreateAPIView): #POST
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductUpdateAPIView(UpdateAPIView): #PUT, PUTCH
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductDestroyAPIView(DestroyAPIView): #DELETE
    queryset = Product.objects.all()  