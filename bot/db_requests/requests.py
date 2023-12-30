import os
import requests

SERVER_HOST = os.getenv('SERVER_HOST')
SERVER_PORT = os.getenv('SERVER_PORT')

def get_user(user_id):
    response= requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/users/{user_id}')
    return response.json()

def add_user_to_db(user_id,user_name):
    requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/users/add_user/{user_id}/{user_name}')

def get_all_meals():
    response= requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/meals/all')
    return response.json()

def get_meal_info(meal_id):
    response= requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/meals/{meal_id}')
    return response.json()

def add_meal_to_account(user_id,meal_id):
    requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/users/{user_id}/add_meals/{meal_id}')

def get_all_products():
    response=requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/search/all')
    return response.json()

def get_meal_with_product(product_id):
    response=requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/search/{product_id}')
    return response.json()
def remove_meal_from_account(user_id,meal_id):
    requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/users/{user_id}/remove_meals/{meal_id}')

def get_meals_with_limit(limit):
    response=requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/search_with_limit/{limit}')
    return response.json()

def delete_all_meals_from_account(user_id):
    requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/users/{user_id}/delete_all_meals')
    
def get_info_about_user_meals(user_id):
    response=requests.get(f'http://{SERVER_HOST}:{SERVER_PORT}/users/get_meals_sum/{user_id}')
    return response.json()