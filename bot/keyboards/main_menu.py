from aiogram.utils.keyboard import InlineKeyboardBuilder
from filters.filters import Favorites,Catalog,Search
#Главное меню
def main_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text='Мой кабинет',callback_data=Favorites())
    builder.button(text='Каталог'    ,callback_data=Catalog())
    builder.button(text='Поиск'      ,callback_data=Search())
    builder.adjust(1)
    return builder.as_markup()
