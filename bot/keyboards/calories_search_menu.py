from aiogram.utils.keyboard import InlineKeyboardBuilder
import filters.filters as filters

def search_product():
    builder=InlineKeyboardBuilder()
    builder.button(text='Назад',callback_data='main_menu')
    builder.adjust(1)
    return builder.as_markup()

def search_not_found():
    builder=InlineKeyboardBuilder()
    builder.button(text='Назад',callback_data='main_menu')
    builder.adjust(1)
    return builder.as_markup()

def search_results(meals,limit):
    builder=InlineKeyboardBuilder()
    for id,meal in meals:
        builder.button(text=f'{meal}',callback_data=filters.MealsActionCaloriesMenu(action='info',meal_id=id,limit=limit))
    builder.button(text="Назад",callback_data='main_menu')
    builder.adjust(1)
    return builder.as_markup()

def action_with_meal(meal_id,limit):#Кнопки для добавления блюда в личный кабинет
    builder = InlineKeyboardBuilder()
    builder.button(text="Добавить",callback_data=filters.MealsActionCaloriesMenu(action='add_to_account',meal_id=meal_id,limit=limit))
    builder.button(text="Назад",callback_data=filters.MealsWithCalories(limit=limit))
    return builder.as_markup()

def action_complete(limit):
    builder=InlineKeyboardBuilder()
    builder.button(text='Назад',callback_data=filters.MealsWithCalories(limit=limit))
    builder.button(text='В главное меню',callback_data='main_menu')
    return builder.as_markup()