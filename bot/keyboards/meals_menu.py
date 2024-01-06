from aiogram.utils.keyboard import InlineKeyboardBuilder
import filters.meals_menu as filters
#Меню заготовленных блюд
def all_meals(meals):
    builder = InlineKeyboardBuilder()
    for id,meal in meals:
        builder.button(text=f'{meal}',callback_data=filters.MealInfo(meal_id=id))
    builder.button(text="Назад",callback_data='main_menu')
    builder.adjust(1)
    return builder.as_markup()

def menu_meal_action(meal_id):
    builder = InlineKeyboardBuilder()
    builder.button(text="Добавить",callback_data=filters.AddMealToFavorites(meal_id=meal_id))
    builder.button(text="Назад",callback_data='meals_menu')
    return builder.as_markup()

def action_complete():
    builder=InlineKeyboardBuilder()
    builder.button(text='Назад',callback_data='meals_menu')
    return builder.as_markup()