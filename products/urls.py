from django.urls import path
from . import views

urlpatterns = [
    path('product/add-product/', views.add_product, name='add-product'),
    path('product/update-product/<str:name>/', views.UpdateProduct, name='update-product'),
    path('product/product-home/', views.home, name='add'),
    path('product/get-categories', views.GetCategories),
    path('product/get-sub-categories', views.GetSubCategories),
    path('shop/<str:name>/<str:vendor>/', views.ProductView),
    path('shop-luxury-fashion-brands/', views.Catalog),
    path('product-category/<str:category>/', views.CategoryView),
    path('product-category/<str:category>/<str:subcategory>/', views.SubCategoryView),
]