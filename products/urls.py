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
    path('search/', views.SearchProductView),
    path('get-brands/', views.Brands),
    path('get-clothing-items/', views.ClothingView),
    path('get-shoe-types/', views.ShoeView),
    path('get-face-and-body-products/', views.FaceAndBodyView),
    path('get-accessory-products/', views.AccessoriesView),
    path('get-beauty-products', views.BeautyProductsView),
    path('get-kid-products/', views.KidsProductsView),
    path('brand/<str:brand_name>/', views.BrandPageView),
    path('brand/<str:brand_name>/<str:category>/', views.StoreProductCategory),
    path('product-category/<str:gender>/clothing/<str:sub_category_clothing>/', views.ProductCategoryByGenderAndClothing),
    path('product-category/<str:gender>/shoe/<str:shoe_sub_category>/', views.ProductCategoryByGenderAndShoe),
    path('product-category/<str:gender>/face-body/<str:face_body_sub_category>/', views.ProductCategoryByGenderAndFaceAndBody),
    path('product-category/<str:gender>/accessories/<str:sub_category_accessory>/', views.ProductCategoryByGenderAndAccessory),
    path('product-category/<str:gender>/beauty/<str:sub_category_beauty>/', views.ProductCategoryByGenderAndBeauty),
]