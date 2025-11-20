from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('',views.home, name="home"),
    # category
    path('add_category/',views.add_category, name="add_category"),
    path('category_list/',views.category_list, name="category_list"),
    
    # products
    path('add_product/',views.add_product, name="add_product"),
    path('product_list/',views.product_list, name="product_list"),
]
