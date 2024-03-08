from django.urls import path

from apps.categorits.views import CategoryListAPI, CategoryCreateAPIView, CategoryUpdateAPIView, CategoryDestroyAPIView

urlpatterns = [
    path('', CategoryListAPI.as_view(), name="api_categories"),
    path('create/', CategoryCreateAPIView.as_view(), name="api_categorits_create"),
    path('update/<int:pk/', CategoryUpdateAPIView.as_view(), name="api_categorits_update"),
    path('destroy/<int:pk/', CategoryDestroyAPIView.as_view(), name="api_categorits_destroy"),
]
