import os
import requests

SERVER_HOST = os.getenv('SERVER_HOST')
SERVER_PORT = os.getenv('SERVER_PORT')

def add_user_to_db(user_id,user_name):
    requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/users/add_user/{user_id}/{user_name}')

def add_meal_to_favorites(user_id,meal_id):
    requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/users/{user_id}/add_meals/{meal_id}')

def delete_all_meals_from_favorites(user_id):
    requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/users/{user_id}/remove_meals/all')

def remove_meal_from_favorites(user_id,meal_id):
    requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/users/{user_id}/remove_meals/{meal_id}')

def get_user_favorites(user_id):
    response= requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/users/{user_id}')
    return response.json()

def get_meals_with_limit(limit):
    response=requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/meals_with_limit/{limit}')
    return response.json()

def get_all_meals():
    response= requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/meals')
    return response.json()

def select_meal(meal_id):
    response= requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/meals/{meal_id}')
    return response.json()

def get_meal_quantity(meal_id):
    response= requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/meals/{meal_id}/quantity')
    return response.json()

def get_all_products():
    response=requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/products')
    return response.json()

def get_meal_with_product(product_id):
    response=requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/products/{product_id}')
    return response.json()

def find_meals_by_name(name):
    response=requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/meals_with_name/{name}')
    return response.json()

def get_sum_of_user_PFC(user_id):
    response=requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/users/sum_of_user_PFC/{user_id}')
    return response.json()