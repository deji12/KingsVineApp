from dataclasses import field
from rest_framework import serializers
from .models import Product, Category, SubCategory, brand, beauty, face_and_body, accessories, clothing, shoe, kids

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = brand
        fields = '__all__'

class BeautySerializer(serializers.ModelSerializer):
    class Meta:
        model = beauty
        fields = '__all__'

class FaceAndBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = face_and_body
        fields = '__all__'

class AccessoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = accessories
        fields = '__all__'

class ClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = clothing
        fields = '__all__'

class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = shoe
        fields = '__all__'

class KidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = kids
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class SubCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'