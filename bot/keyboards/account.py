from aiogram.utils.keyboard import InlineKeyboardBuilder
from filters.filters import Favorites,DeleteAllFromFavorites,GetMealInfo,DeleteFromFavorites,MainMenu
#Кнопки с названиями блюд добавленных пользователем в кабинет
def user_meals(meals):
    builder=InlineKeyboardBuilder()
    for id,meal in meals:
        builder.button(text=f'{meal}',callback_data=GetMealInfo(meal_id=id,menu='favorites'))
    builder.button(text="Удалить все",callback_data=DeleteAllFromFavorites())
    builder.button(text="Назад",callback_data=MainMenu())
    builder.adjust(1)
    return builder.as_markup()

#Кнопки для работы с блюдами добавленными пользователем в кабинет
def user_meals_action(id):
    builder=InlineKeyboardBuilder()
    builder.button(text="Удалить",callback_data=DeleteFromFavorites(meal_id=id))
    builder.button(text='Назад',callback_data=Favorites())
    return builder.as_markup()

def action_complete():
    builder=InlineKeyboardBuilder()
    builder.button(text='Назад',callback_data=Favorites())
    return builder.as_markup()