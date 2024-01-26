from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from filters.filters import GetMealInfo,AddMealToFavorites,Catalog,MealCatalog,MainMenu
#Меню заготовленных блюд
def all_meals(meals):
    builder = InlineKeyboardBuilder()
    for id,meal in meals:
        builder.button(text=f'{meal}',callback_data=GetMealInfo(meal_id=id,menu='meals_menu'))
    builder.button(text="Назад",callback_data=Catalog())
    builder.adjust(1)
    return builder.as_markup()

def menu_meal_action(meal_id):
    builder = InlineKeyboardBuilder()
    builder.button(text="Добавить",callback_data=AddMealToFavorites(meal_id=meal_id,menu='meals_menu'))
    builder.button(text="Назад",callback_data=MealCatalog())
    return builder.as_markup()

def action_complete():
    builder=InlineKeyboardBuilder()
    builder.button(text='Назад',callback_data=MealCatalog())
    builder.button(text='В главное меню',callback_data=MainMenu())
    return builder.as_markup()