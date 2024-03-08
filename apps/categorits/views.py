from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from apps.categorits.models import Categorits
from apps.categorits.serializers import CategoritsSerializer

# Create your views here.
class CategoryListAPI(ListAPIView):
    queryset = Categorits.objects.all()
    serializer_class = CategoritsSerializer
    
class CategoryCreateAPIView(CreateAPIView): 
    queryset = Categorits.objects.all()
    serializer_class = CategoritsSerializer
    
class CategoryUpdateAPIView(UpdateAPIView): 
    queryset = Categorits.objects.all()
    serializer_class = CategoritsSerializer
    
class CategoryDestroyAPIView(DestroyAPIView): 
    queryset = Categorits.objects.all()