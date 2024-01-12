from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from filters.filters import MainMenu,MealCatalog,ProductCatalog

def chose_catalog():
    builder = InlineKeyboardBuilder()
    builder.button(text='Каталог блюд',callback_data=MealCatalog())
    builder.button(text='Каталог ингридиентов',callback_data=ProductCatalog())
    builder.button(text="Назад",callback_data=MainMenu())
    builder.adjust(1)
    return builder.as_markup()
