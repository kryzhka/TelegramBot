from aiogram.utils.keyboard import InlineKeyboardBuilder
from filters.filters import Search,GetMealInfo,MainMenu,AddMealToFavorites,FoundedMeals

def search_meal():
    builder=InlineKeyboardBuilder()
    builder.button(text='Назад',callback_data=Search())
    builder.adjust(1)
    return builder.as_markup()

def search_results(meals,name):
    builder=InlineKeyboardBuilder()
    for id,meal in meals:
        builder.button(text=f'{meal}',callback_data=GetMealInfo(meal_id=id,name=name,menu='meal_name_search'))
    builder.button(text="Назад",callback_data=Search())
    builder.adjust(1)
    return builder.as_markup()

def search_not_found():
    builder=InlineKeyboardBuilder()
    builder.button(text='Назад',callback_data=MainMenu())
    builder.adjust(1)
    return builder.as_markup()

def action_with_meal(meal_id,name):#Кнопки для добавления блюда в личный кабинет
    builder = InlineKeyboardBuilder()
    builder.button(text="Добавить",callback_data=AddMealToFavorites(meal_id=meal_id,menu='meal_name_search',name=name))
    builder.button(text="Назад",callback_data=FoundedMeals(name=name))
    return builder.as_markup()

def action_complete(name):
    builder=InlineKeyboardBuilder()
    builder.button(text='Назад',callback_data=FoundedMeals(name=name))
    builder.button(text='В главное меню',callback_data=MainMenu())
    return builder.as_markup()