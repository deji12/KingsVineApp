from django.test import TestCase

# Create your tests here.
import requests
import json
url = 'http://127.0.0.1:8000/auth/create-user/'

response = requests.post(
    url,
#     headers = {
#     'Content-Type': 'multipart/form-data',
#   },
    json = {
        'email': 'theprotongtuy@yahoo.com',
        'username': 'rick',
        'password':'bill6789',
        'confirm_password':'billieeilish',
        'first_name': 'ayo',
        'last_name': 'deji',
        'shop_name': 'The proton shop',
        'role': 'customer',
        'shop_url': 'https://www.theprotonguy.herokuapp.com'
    },
)

print(response._content)
# print(response._content.decode().split(",")[1])
# print(response._content.decode()[14:40])

# login_url = 'http://127.0.0.1:8000/auth/token/login'
# response = requests.post(
#     login_url,
#     json  = {
#         'email': 'theprotonguy@yahoo.com',
#         'password': 'iwillbegreat',
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

#retrieve users

# users = 'http://127.0.0.1:8000/auth/all-users'

# response = requests.get(
#     users,
#     headers = {
#         'authorization': 'Token 70629d87dcd5c4efa4c2b223aedd27b99a761c00'
#     }
# )

# print(response._content)


#adding shipping details
# users = 'http://127.0.0.1:8000/customers/add-shipping-address/'

# response = requests.post(
#     users,
#     json  = {
#         'user': 'tpg',
#         'first_name': 'ayo',
#         'last_name': 'deji',
#         'company_name': 'THE PROTON GUY',
#         'country': 'Nigeria',
#         'street_address1': 'Vgc, road 3 close 2',
#         'street_address2': 'house j15 lekki lagos',
#         'town_city': 'lagos',
#         'state': 'lagos',
#         'postcode_zip': '12345'
#     },
#     # headers = {
#     #     'authorization': 'Token 04dc7d075bc488f4ee23d1ef4ea8943bb0e4a4e4'
#     # }
# )

# print(response._content)

# # get shipping address
# users = 'http://127.0.0.1:8000/customers/user-shipping-address/'

# response = requests.get(
#     users,
#     headers = {
#         'authorization': 'Token 04dc7d075bc488f4ee23d1ef4ea8943bb0e4a4e4'
#     }
# )

# print(response._content)


#adding billing details
# users = 'http://127.0.0.1:8000/customers/add-billing-address/'

# response = requests.post(
#     users,
#     json  = {
#         'user': 'tpg',
#         'first_name': 'ayo',
#         'last_name': 'deji',
#         'company_name': 'THE PROTON GUY',
#         'country': 'Nigeria',
#         'street_address1': 'Vgc, road 3 close 2',
#         'street_address2': 'house j15 lekki lagos',
#         'town_city': 'lagos',
#         'state': 'lagos',
#         'postcode_zip': '12345',
#         'phone': '08141783687',
#         'email': 'adesolaayodeji18@gmail.com'
#     },
#     # headers = {
#     #     'authorization': 'Token 04dc7d075bc488f4ee23d1ef4ea8943bb0e4a4e4'
#     # }
# )

# print(response._content)


# # get billing address
# users = 'http://127.0.0.1:8000/customers/user-billing-address/'

# response = requests.get(
#     users,
#     headers = {
#         'authorization': 'Token 04dc7d075bc488f4ee23d1ef4ea8943bb0e4a4e4'
#     }
# )

# print(response._content)



#user password update
# url = 'http://127.0.0.1:8000/auth/update-user-password/'
# response = requests.post(
#     url,
#     headers = {
#         'authorization': 'Token 6278caec3eef46193cedf4cf0a1355780fe8b832'
#     },
#     json = {
        
#         'password':'iwillbegreat',
#         'newpassword': 'billieeilish',
#         'confirmpassword':'billieeilish',
       
#     },
    
# )

# print(response._content)

# url = 'http://127.0.0.1:8000/auth/users/set_password/'
# response = requests.post(
#     url,
#     headers = {
#         'authorization': 'Token 70629d87dcd5c4efa4c2b223aedd27b99a761c00'
#     },
#     json = {
        
#         'current_password':'billieeilish',
#         'new_password': 'iwillbegreat',
#         're_password':'iwillbegreat',
       
#     },
    
# )

# print(response._content)









# update user profile
# url = 'http://127.0.0.1:8000/auth/update-user-profile/'
# response = requests.put(
#     url,
#     headers = {
#         'authorization': 'Token b58ec67f2ecb4f5d024e4448caa0918690dc5171'
#     },
#     json = {
        
#         'username':'eilish',
#         'email': 'billie@gmail.com',
#         'first_name':'finneas',
       
#     },
    
# )

# print(response._content)