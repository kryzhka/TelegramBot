from aiogram.utils.keyboard import InlineKeyboardBuilder
from filters.filters import MainMenu,MealNameSearch,ProductSearch,CaloriesSearch,GetAllProducts,ProductNameSearch,Search

def search_menu():
    builder=InlineKeyboardBuilder()
    builder.button(text='Поиск по названию',callback_data=MealNameSearch())
    builder.button(text='Поиск по ингридиенту',callback_data=ProductSearch())
    builder.button(text='Поиск по количеству калорий',callback_data=CaloriesSearch())
    builder.button(text='Назад',callback_data=MainMenu())
    builder.adjust(1)
    return builder.as_markup()

def product_search_menu():#Кнопки для корневого меню поиска
    builder=InlineKeyboardBuilder()
    builder.button(text='Все доступные ингридиенты',callback_data=GetAllProducts())
    builder.button(text='Поиск по названию',callback_data=ProductNameSearch())
    builder.button(text="Назад",callback_data=Search())
    builder.adjust(1)
    return builder.as_markup()