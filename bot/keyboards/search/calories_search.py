from aiogram.utils.keyboard import InlineKeyboardBuilder
from filters.filters import Search,MainMenu,GetMealInfo,AddMealToFavorites,MealsWithCalories

def search_product():
    builder=InlineKeyboardBuilder()
    builder.button(text='Назад',callback_data=Search())
    builder.adjust(1)
    return builder.as_markup()

def search_not_found():
    builder=InlineKeyboardBuilder()
    builder.button(text='Назад',callback_data=MainMenu())
    builder.adjust(1)
    return builder.as_markup()

def search_results(meals,limit):
    builder=InlineKeyboardBuilder()
    for id,meal in meals:
        builder.button(text=f'{meal}',callback_data=GetMealInfo(meal_id=id,limit=limit,menu='calories_search'))
    builder.button(text="Назад",callback_data=Search())
    builder.adjust(1)
    return builder.as_markup()

def action_with_meal(meal_id,limit):#Кнопки для добавления блюда в личный кабинет
    builder = InlineKeyboardBuilder()
    builder.button(text="Добавить",callback_data=AddMealToFavorites(meal_id=meal_id,menu='calories_search',limit=limit))
    builder.button(text="Назад",callback_data=MealsWithCalories(limit=limit))
    return builder.as_markup()

def action_complete(limit):
    builder=InlineKeyboardBuilder()
    builder.button(text='Назад',callback_data=MealsWithCalories(limit=limit))
    builder.button(text='В главное меню',callback_data=MainMenu())
    return builder.as_markup()