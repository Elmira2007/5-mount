from django.urls import path

from apps.products.views import ProductListAPI, ProductCreateAPIView, ProductUpdateAPIView, ProductDestroyAPIView

urlpatterns = [
    path('', ProductListAPI.as_view(), name="api_products"),
    path('create/', ProductCreateAPIView.as_view(), name="api_products_create"),
    path('update/<int:pk/', ProductUpdateAPIView.as_view(), name="api_products_updape"),
    path('delete/', ProductDestroyAPIView.as_view(), name="api_products_delete"),
]
