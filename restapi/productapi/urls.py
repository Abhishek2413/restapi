from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('api/products', ProductListView.as_view()),
    path('api/products/<int:pid>',ProductDetailView.as_view()),
]


