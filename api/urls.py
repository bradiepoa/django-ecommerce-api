from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.getRoutes, name="routes"),
    path('products/', views.getProducts, name="products"),
    path('product/<str:pk>/', views.getProduct, name="product"),
    path('categories/', views.getCategories, name="categories"),
    path('category/<str:pk>/', views.getCategory, name="category")
]