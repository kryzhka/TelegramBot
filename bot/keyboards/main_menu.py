from aiogram.utils.keyboard import InlineKeyboardBuilder
import filters.filters as filters
#Главное меню
def main_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text='Мой кабинет',callback_data='favorites')
    builder.button(text='Все доступные блюда',callback_data='meals_menu')
    builder.button(text='Поиск по ингридиенту',callback_data='search_menu')
    builder.button(text='Поиск по количеству калорий',callback_data='calories_search_menu')
    builder.adjust(1)
    return builder.as_markup()
