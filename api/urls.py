from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.getRoutes, name="routes"),
    path('products/', views.getProducts, name="products"),
    path('product/<str:pk>/', views.getProduct, name="product"),
    path('categories/', views.getCategories, name="categories"),
    path('category/<str:pk>/', views.getCategory, name="category"),
    # orders
    path('orders/', views.getOrders, name="orders"),
    path('order/<str:pk>/', views.getOrder, name="order"),
    path('orderitems/', views.getOrderItems, name="orderitems"),
    path('orderitem/<str:pk>/', views.getOrderItem, name="orderitem"),
    path('shippingaddress/', views.getShippingAddresses, name="shippingaddress"),
    path('shippingaddres/<str:pk>/', views.getShippingAddress, name="shippingaddres"),
]