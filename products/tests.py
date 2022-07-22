from django.test import TestCase
import requests
import base64

# Create your tests here.
# login_url = 'http://127.0.0.1:8000/auth/token/login'
# response = requests.post(
#     login_url,
#     json  = {
#         'email': 'adesolaayodeji18@gmail.com',
#         'password': 'admin',
#     }
# )

# print(response._content)

# logout_url = 'http://127.0.0.1:8000/auth/token/logout'
# response = requests.post(
#     logout_url,
#     headers = {
#         'authorization': 'Token b6972e2a06b2508931308ceec22e1e436208ad52'
#     },
# )

# print(response._content)


#add product
# url = 'http://127.0.0.1:8000/products/update-product/Robot/'

# files = {'image1': open('C:/Users/macbook/Desktop/umm.jpg', 'rb')}

# response = requests.put(
#     url,
#     headers = {
#         'authorization': 'Token fe036843608f4d6965cfc23ea073417be6c55866',        
#     },
#     json = {
#         'product_name': 'Change',
#         'price': '50',
#         'discounted_price': '25',
#         'description': 'This is a change',
#         'category': 'Women',
#         'sub_category': 'Dress',
#         'tags': 'test, yo'
#     },
#     # files=files
# )

# print(response._content)

url = 'http://127.0.0.1:8000/product-category/Tech/Robot/'

response = requests.get(
    url,
    # headers = {
    #     'authorization': 'Token fe036843608f4d6965cfc23ea073417be6c55866',        
    # },
    # json = {
    #     'sort_type': 'Sort by price: low to high'
    # }
)
print(response._content)