from django.shortcuts import render
from .serializers import AccessoriesSerializer, ProductSerializer, SubCategoriesSerializer, CategoriesSerializer, BrandSerializer, BeautySerializer, FaceAndBodySerializer, ClothingSerializer, KidsSerializer, ShoeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from kvapp.models import User
from products import serializers
from .models import Product, Category, SubCategory, brand, beauty, face_and_body, clothing, shoe, accessories, kids
from django.core.mail import EmailMessage
from django.conf import settings
import datetime


#view for adding new products to database
@api_view(['POST', 'PUT'])
@permission_classes([IsAuthenticated])
def add_product(request):
    if request.method == 'POST':
        get_user = User.objects.get(email=request.user.email)
        #grab data for validation by serializer
        data_context = {
            'vendor': get_user.pk,
            'name': request.data.get('product_name'),
            'price': request.data.get('price'),
            'discounted_price': request.data.get('discounted_price'),
            'description': request.data.get('description'),
            'category': Category.objects.get(name=request.data.get('category')).pk,
            'sub_category': SubCategory.objects.get(sub_category_name=request.data.get('sub_category')).pk,
            'tags': request.data.get('tag'),
            'image1': request.data.get('image1'),
        }
        serializer = ProductSerializer(data=data_context)

        if serializer.is_valid():
            #save product if product data is valid
            new_product = Product(
                vendor =  get_user,
                name = request.data.get('product_name'),
                price = request.data.get('price'),
                discounted_price = request.data.get('discounted_price'),
                description = request.data.get('description'),
                tags = request.data.get('tag'),
                image1 = request.data.get('image1'),
            )

            #check for what gender product is coming in
            if request.data.get('category') == 'Women':
                new_product.category = Category.objects.get(name=request.data.get('category'))
                new_product.sub_category = SubCategory.objects.get(sub_category_name=request.data.get('sub_category'))
                new_product.gender = 'female'
            elif request.data.get('category') == 'Men':
                new_product.category = Category.objects.get(name=request.data.get('category'))
                new_product.sub_category = SubCategory.objects.get(sub_category_name=request.data.get('sub_category'))
                new_product.gender = 'male'
            #if product is gender neutral
            else:
                new_product.category = Category.objects.get(name=request.data.get('category'))
                if request.data.get('sub_category'):
                    #checking if product has a sub category
                    new_product.sub_category = SubCategory.objects.get(sub_category_name=request.data.get('sub_category'))
            new_product.save()

            #send email to admin to verify product
            email_mess = EmailMessage (
                f'KV APP: Product Verification',
                f'Vendor: {get_user} \n \n View Product: http://127.0.0.1:8000/admin/products/product/{new_product.id}/change/ \n \n Date: {datetime.datetime.now()}',
                settings.EMAIL_HOST_USER,
                ['adesolaayodeji53@gmail.com']
            )
            email_mess.fail_silently = True
            email_mess.send()
            return Response({'Message': 'Product successfully added, It is under verification'})

        else:
            data = serializer.errors
            return Response(data)


#view to update products
@api_view(['PUT']) #post, put 
@permission_classes([IsAuthenticated])
def UpdateProduct(request, name):
    if request.method == 'PUT':
        get_user = User.objects.get(email=request.user.email)
        
        
        #creating a dictionary containing incoming data to be validated by serializer
        data_context = {
            'vendor': get_user.pk,
        }

        #saving incoming data to dictionary
        if request.data.get('product_name'):
            data_context["name"] = request.data.get('product_name')
        if request.data.get('price'):
            data_context["price"] = request.data.get('price')
        if request.data.get('discounted_price'):
            data_context['discounted_price'] = request.data.get('discounted_price')
        if request.data.get('category'):
            data_context['category'] = Category.objects.get(name=request.data.get('category')).pk
        if request.data.get('sub_category'):
            data_context['sub_category'] = SubCategory.objects.get(sub_category_name=request.data.get('sub_category')).pk
        if request.data.get('tag'):
            data_context['tags'] = request.data.get('tag')
        if request.data.get('short_description'):
            data_context['short_description'] = request.data.get('short_description')
        if request.data.get('description'):
            data_context['description'] = request.data.get('description')
        if request.data.get('purcase_note'):
            data_context['purchase_note'] = request.data.get('purcase_note')
        if request.data.get('visibility'):
            data_context['visibility'] = request.data.get('visibility')
        if request.data.get('product_reviews'):
            data_context['product_reviews'] = request.data.get('product_reviews')
        if request.data.get('image1'):
            data_context['image1'] = request.data.get('image1')
        if request.data.get('image2'):
            data_context['image2'] = request.data.get('image2')
        if request.data.get('image3'):
            data_context['image3'] = request.data.get('image3')
        if request.data.get('image4'):
            data_context['image4'] = request.data.get('image4')
        if request.data.get('image5'):
            data_context['image5'] = request.data.get('image5')
        
        serializer = ProductSerializer(data=data_context)
        #validating data
        if serializer.is_valid():
            #getting particular product to be updated
            get_product = Product.objects.get(name=name, vendor=get_user)

            #checking for data that came through and saving
            if request.data.get('product_name'):
               get_product.name = request.data.get('product_name')

            if request.data.get('price'):
                get_product.price = request.data.get('price')

            if request.data.get('discounted_price'):
                get_product.discounted_price = request.data.get('discounted_price')

            if request.data.get('description'):
                get_product.description = request.data.get('description')

            if request.data.get('category'):
                get_product.category = Category.objects.get(name=request.data.get('category'))

            if request.data.get('sub_category'):
                get_product.sub_category = SubCategory.objects.get(sub_category_name=request.data.get('sub_category'))

            if request.data.get('tag'):
                get_product.tag = request.data.get('tag')

            if request.data.get('short_description'):
                get_product.short_description = request.data.get('short_description')
            
            if request.data.get('purcase_note'):
                get_product.purchase_note = request.data.get('purchase_note')

            if request.data.get('visibility'):
                get_product.visibility = request.data.get('visibility')

            if request.data.get('product_reviews'):
                get_product.product_reviews = request.data.get('product_reviews')
            
            if request.data.get('image1'):
                get_product.image1 = request.data.get('image1')
            
            if request.data.get('image2'):
                get_product.image2 = request.data.get('image2')

            if request.data.get('image3'):
                get_product.image3 = request.data.get('image3')

            if request.data.get('image4'):
                get_product.image4 = request.data.get('image4')

            if request.data.get('image5'):
                get_product.image5 = request.data.get('image5')
            
            #saving changes and returning response to client
            get_product.save()
            return Response({'Message': 'Product successfully updated.'})
        #if serializer is not valid, return errors encountered
        else:
            data = serializer.errors
            return Response(data)

def home(request):
    if request.method == 'POST':
        print('yessss')
        print(request.data)
    return render(request, 'products/index.html')

#get categories for product creation
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetCategories(request):
    all_categories = Category.objects.all()
    serializer = CategoriesSerializer(data=all_categories, many=True)
    return Response(serializer.data)

#get sub categories for product creation
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetSubCategories(request):
    all_sub_categories = SubCategory.objects.all()
    serializer = SubCategoriesSerializer(data=all_sub_categories, many=True)
    return Response(serializer.data)

#view for product view page
@api_view(['GET'])
def ProductView(request, name, vendor):
    #get vendor model
    get_vendor = User.objects.get(email=vendor)
    #get product for display in frontend
    get_product = Product.objects.get(vendor=get_vendor, name=name)
    #serialize queryset
    serializer = ProductSerializer(data=get_product)
    return Response(serializer.data)

#catalog page
@api_view(['GET', 'POST'])
def Catalog(request):
    if request.method == 'POST':
        sort = request.data.get('sort_type')
        if sort == 'Sort by popularity':
            get_products_by_popularty = Product.objects.all().order_by('-clicks')[:36]
            serializer = ProductSerializer(get_products_by_popularty, many=True)
            return Response(serializer.data)
        elif sort == 'Sort by latest':
            get_products = Product.objects.all().order_by('-date_created')[:36]
            serializer = ProductSerializer(get_products, many=True)
            return Response(serializer.data)
        elif sort == 'Sort by price: low to high':
            get_products = Product.objects.all().order_by('price')[:36]
            serializer = ProductSerializer(get_products, many=True)
            return Response(serializer.data)
        elif sort == 'Sort by price: high to low':
            get_products = Product.objects.all().order_by('-price')[:36]
            serializer = ProductSerializer(get_products, many=True)
            return Response(serializer.data)

    get_products = Product.objects.all().order_by('-clicks')[:36]
    serializer = ProductSerializer(get_products, many=True)
    return Response(serializer.data)
 
#view for getting products by their category
@api_view(['GET'])
def CategoryView(request, category):
    get_category = Category.objects.get(name=category)
    get_products_by_category = Product.objects.get(category=get_category)
    serializer = ProductSerializer(get_products_by_category, many=True)
    return Response(serializer.data)

#view for getting products by their category and sub category
@api_view(['GET'])
def SubCategoryView(request, category, subcategory):
    get_category = Category.objects.get(name=category)
    get_sub_category = SubCategory.objects.get(category=get_category, sub_category_name=subcategory)
    get_products_by_sub_category = Product.objects.filter(category=get_category, sub_category=get_sub_category)
    serializer = ProductSerializer(get_products_by_sub_category, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def SearchProductView(request):
    search_value = request.data.get('search')
    filter_for_product_containing_search_name = Product.objects.filter(name__icontains=search_value).order_by('-date_created')
    if filter_for_product_containing_search_name:
        serializer = ProductSerializer(filter_for_product_containing_search_name, many=True)
        return Response(serializer.data)
    else:
        return Response(f'Sorry, but nothing matched your search terms. Please try again with some different keywords.')

@api_view(['GET'])
def Brands(request):
    all_brands = brand.objects.all()[:15]
    serializer = BrandSerializer(all_brands, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ClothingView(request):
    all_clothing = clothing.objects.all()[:15]
    serializer = ClothingSerializer(all_clothing, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ShoeView(request):
    all_shoes = shoe.objects.all()[:15]
    serializer = ShoeSerializer(all_shoes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def FaceAndBodyView(request):
    all_face_and_body_products = face_and_body.objects.all()[:15]
    serializer = FaceAndBodySerializer(all_face_and_body_products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def AccessoriesView(request):
    all_accessories = accessories.objects.all()[:15]
    serializer = AccessoriesSerializer(all_accessories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def BeautyProductsView(request):
    all_beauty_products = beauty.objects.all()[:15]
    serializer = BeautySerializer(all_beauty_products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def KidsProductsView(request):
    all_kid_products = kids.objects.all()[:15]
    serializer = KidsSerializer(all_kid_products, many=True)
    return Response(serializer.data)

#view for displaying goods of a SINGLE BRAND
@api_view(['GET', 'POST'])
def BrandPageView(request, brand_name):
    if request.method == 'POST':
        # return products based on sorting method by user
        sort = request.data.get('sort_type')
        if sort:
            if sort == 'Sort by popularity':
                get_products_by_popularty = Product.objects.filter(brand=brand_name).order_by('-clicks')[:36]
                serializer = ProductSerializer(get_products_by_popularty, many=True)
                return Response(serializer.data)
            elif sort == 'Sort by latest':
                get_products = Product.objects.filter(brand=brand_name).order_by('-date_created')[:36]
                serializer = ProductSerializer(get_products, many=True)
                return Response(serializer.data)
            elif sort == 'Sort by price: low to high':
                get_products = Product.objects.filter(brand=brand_name).order_by('price')[:36]
                serializer = ProductSerializer(get_products, many=True)
                return Response(serializer.data)
            elif sort == 'Sort by price: high to low':
                get_products = Product.objects.filter(brand=brand_name).order_by('-price')[:36]
                serializer = ProductSerializer(get_products, many=True)
                return Response(serializer.data)
        else:
            pass

        # send email from contact vendor form
        if request.data.get('name-input'):
            # get data from contact form
            name = request.data.get('name-input')
            email = request.data.get('email')
            body = request.data.get('body')
            email_mess = EmailMessage (
                f'KV APP: Contact Vendor Form',
                f'Contact Vendor Form \n \n From: \n \n Name: {name} \n Email: {email} \n Body: {body}', #message
                settings.EMAIL_HOST_USER,
                ['adesolaayodeji53@gmail.com'] #receiver
            )
            email_mess.fail_silently = True
            #send email
            email_mess.send()
            return Response({'Message': 'Product successfully added, It is under verification'})


        # return products based on user search input
        search_value = request.data.get('search')
        if search_value:
            filter_for_product_containing_search_name = Product.objects.filter(brand=brand_name, name__icontains=search_value).order_by('-date_created')
            if filter_for_product_containing_search_name:
                serializer = ProductSerializer(filter_for_product_containing_search_name, many=True)
                return Response(serializer.data)
            else:
                return Response(f'Sorry, but nothing matched your search terms. Please try again with some different keywords.')

    get_products_by_brand = Product.objects.filter(brand=brand_name)
    serializer = ProductSerializer(get_products_by_brand, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def StoreProductCategory(request, brand_name, category):
    get_category = Category.objects.get(name=category)
    get_products_by_brand_and_category = Product.objects.filter(category=get_category, brand=brand_name)
    serializer = ProductSerializer(get_products_by_brand_and_category, many=True)
    return Response(serializer.data)

#view products by gender and clothing type
@api_view(['GET', 'POST'])
def ProductCategoryByGenderAndClothing(request, gender, sub_category_clothing):
    get_category = Category.objects.get(name='Clothing')
    get_sub_category = SubCategory.objects.get(category=get_category, sub_category_name=sub_category_clothing)
    get_product_by_gender_and_clothing_type = Product.objects.filter(gender=gender, category=get_category, sub_category=get_sub_category)

    if request.method == 'POST':
        # return products based on sorting method by user
        sort = request.data.get('sort_type')
        if sort:
            if sort == 'Sort by popularity':
                get_products_by_popularty = Product.objects.filter(gender=gender, category=get_category, sub_category=get_sub_category).order_by('-clicks')[:36]
                serializer = ProductSerializer(get_products_by_popularty, many=True)
                return Response(serializer.data)
            elif sort == 'Sort by latest':
                get_products = Product.objects.filter(gender=gender, category=get_category, sub_category=get_sub_category).order_by('-date_created')[:36]
                serializer = ProductSerializer(get_products, many=True)
                return Response(serializer.data)
            elif sort == 'Sort by price: low to high':
                get_products = Product.objects.filter(gender=gender, category=get_category, sub_category=get_sub_category).order_by('price')[:36]
                serializer = ProductSerializer(get_products, many=True)
                return Response(serializer.data)
            elif sort == 'Sort by price: high to low':
                get_products = Product.objects.filter(gender=gender, category=get_category, sub_category=get_sub_category).order_by('-price')[:36]
                serializer = ProductSerializer(get_products, many=True)
                return Response(serializer.data)
        else:
            pass
    
    serializer = ProductSerializer(get_product_by_gender_and_clothing_type, many=True)
    return Response(serializer.data)\

#view products by gender and show type
@api_view(['GET', 'POST'])
def ProductCategoryByGenderAndShoe(request, gender, shoe_sub_category):
    get_category = Category.objects.get(name='Shoe')
    get_sub_category = SubCategory.objects.get(category=get_category, sub_category_name=shoe_sub_category)
    get_product_by_gender_and_shoe_type = Product.objects.filter(gender=gender, sub_category=get_sub_category)
    if request.method == 'POST':
        # return products based on sorting method by user
        sort = request.data.get('sort_type')
        if sort:
            if sort == 'Sort by popularity':
                get_products_by_popularty = Product.objects.filter(gender=gender, sub_category=get_sub_category).order_by('-clicks')[:36]
                serializer = ProductSerializer(get_products_by_popularty, many=True)
                return Response(serializer.data)
            elif sort == 'Sort by latest':
                get_products = Product.objects.filter(gender=gender, sub_category=get_sub_category).order_by('-date_created')[:36]
                serializer = ProductSerializer(get_products, many=True)
                return Response(serializer.data)
            elif sort == 'Sort by price: low to high':
                get_products = Product.objects.filter(gender=gender, sub_category=get_sub_category).order_by('price')[:36]
                serializer = ProductSerializer(get_products, many=True)
                return Response(serializer.data)
            elif sort == 'Sort by price: high to low':
                get_products = Product.objects.filter(gender=gender, sub_category=get_sub_category).order_by('-price')[:36]
                serializer = ProductSerializer(get_products, many=True)
                return Response(serializer.data)
        else:
            pass
    
    serializer = ProductSerializer(get_product_by_gender_and_shoe_type, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def ProductCategoryByGenderAndFaceAndBody(request, gender, face_body_sub_category):
    get_category = Category.objects.get(name='Face & Body')
    get_sub_category = SubCategory.objects.get(category=get_category, sub_category_name=face_body_sub_category)
    get_product_by_gender_and_face_body_product = Product.objects.filter(gender=gender, sub_category=get_sub_category)
    if request.method == 'POST':
        # return products based on sorting method by user
        sort = request.data.get('sort_type')
        if sort:
            if sort == 'Sort by popularity':
                get_products_by_popularty = Product.objects.filter(gender=gender, sub_category=get_sub_category).order_by('-clicks')[:36]
                serializer = ProductSerializer(get_products_by_popularty, many=True)
                return Response(serializer.data)
            elif sort == 'Sort by latest':
                get_products = Product.objects.filter(gender=gender, sub_category=get_sub_category).order_by('-date_created')[:36]
                serializer = ProductSerializer(get_products, many=True)
                return Response(serializer.data)
            elif sort == 'Sort by price: low to high':
                get_products = Product.objects.filter(gender=gender, sub_category=get_sub_category).order_by('price')[:36]
                serializer = ProductSerializer(get_products, many=True)
                return Response(serializer.data)
            elif sort == 'Sort by price: high to low':
                get_products = Product.objects.filter(gender=gender, sub_category=get_sub_category).order_by('-price')[:36]
                serializer = ProductSerializer(get_products, many=True)
                return Response(serializer.data)
        else:
            pass
    
    serializer = ProductSerializer(get_product_by_gender_and_face_body_product, many=True)
    return Response(serializer.data)
    
@api_view(['GET', 'POST'])
def ProductCategoryByGenderAndAccessory(request, gender, sub_category_accessory):
    get_category = Category.objects.get(name='Accessories')
    get_sub_category = SubCategory.objects.get(category=get_category, sub_category_name=sub_category_accessory)
    get_product_by_gender_and_accessory = Product.objects.filter(gender=gender, sub_category=get_sub_category)
    if request.method == 'POST':
        # return products based on sorting method by user
        sort = request.data.get('sort_type')
        if sort:
            if sort == 'Sort by popularity':
                get_products_by_popularty = Product.objects.filter(gender=gender, sub_category=get_sub_category).order_by('-clicks')[:36]
                serializer = ProductSerializer(get_products_by_popularty, many=True)
                return Response(serializer.data)
            elif sort == 'Sort by latest':
                get_products = Product.objects.filter(gender=gender, sub_category=get_sub_category).order_by('-date_created')[:36]
                serializer = ProductSerializer(get_products, many=True)
                return Response(serializer.data)
            elif sort == 'Sort by price: low to high':
                get_products = Product.objects.filter(gender=gender, sub_category=get_sub_category).order_by('price')[:36]
                serializer = ProductSerializer(get_products, many=True)
                return Response(serializer.data)
            elif sort == 'Sort by price: high to low':
                get_products = Product.objects.filter(gender=gender, sub_category=get_sub_category).order_by('-price')[:36]
                serializer = ProductSerializer(get_products, many=True)
                return Response(serializer.data)
        else:
            pass
    
    serializer = ProductSerializer(get_product_by_gender_and_accessory, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def ProductCategoryByGenderAndBeauty(request, gender, sub_category_beauty):
    get_category = Category.objects.get(name='Beauty')
    get_sub_category = SubCategory.objects.get(category=get_category, sub_category_name=sub_category_beauty)
    get_product_by_gender_and_beauty = Product.objects.filter(gender=gender, sub_category=get_sub_category)
    if request.method == 'POST':
        # return products based on sorting method by user
        sort = request.data.get('sort_type')
        if sort:
            if sort == 'Sort by popularity':
                get_products_by_popularty = Product.objects.filter(gender=gender, sub_category=get_sub_category).order_by('-clicks')[:36]
                serializer = ProductSerializer(get_products_by_popularty, many=True)
                return Response(serializer.data)
            elif sort == 'Sort by latest':
                get_products = Product.objects.filter(gender=gender, sub_category=get_sub_category).order_by('-date_created')[:36]
                serializer = ProductSerializer(get_products, many=True)
                return Response(serializer.data)
            elif sort == 'Sort by price: low to high':
                get_products = Product.objects.filter(gender=gender, sub_category=get_sub_category).order_by('price')[:36]
                serializer = ProductSerializer(get_products, many=True)
                return Response(serializer.data)
            elif sort == 'Sort by price: high to low':
                get_products = Product.objects.filter(gender=gender, sub_category=get_sub_category).order_by('-price')[:36]
                serializer = ProductSerializer(get_products, many=True)
                return Response(serializer.data)
        else:
            pass
    
    serializer = ProductSerializer(get_product_by_gender_and_beauty, many=True)
    return Response(serializer.data)