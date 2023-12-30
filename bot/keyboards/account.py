from aiogram.utils.keyboard import InlineKeyboardBuilder
import filters.filters as filters
#Кнопки с названиями блюд добавленных пользователем в кабинет
def user_meals(meals):
    builder=InlineKeyboardBuilder()
    for id,meal in meals:
        builder.button(text=f'{meal}',callback_data=filters.AccountActionWithMeal(action='info_about_meal',meal_id=id))
    builder.button(text="Назад",callback_data='main_menu')
    builder.button(text="Удалить все",callback_data=filters.AccountActionWithAllMeal(action='delete_all'))
    builder.adjust(1)
    return builder.as_markup()

#Кнопки для работы с блюдами добавленными пользователем в кабинет
def user_meals_action(id):
    builder=InlineKeyboardBuilder()
    builder.button(text="Удалить",callback_data=filters.AccountActionWithMeal(action='delete',meal_id=id))
    builder.button(text='Назад',callback_data=filters.AccountActionWithAllMeal(action='info'))
    return builder.as_markup()

def action_complete():
    builder=InlineKeyboardBuilder()
    builder.button(text='Назад',callback_data=filters.AccountActionWithAllMeal(action='info'))
    return builder.as_markup()