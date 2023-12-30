from aiogram.utils.keyboard import InlineKeyboardBuilder
import filters.filters as filters
#Поиск

def search_menu():#Кнопки для корневого меню поиска
    builder=InlineKeyboardBuilder()
    builder.button(text='Все доступные ингридиенты',callback_data='all_products')
    builder.button(text='Поиск по названию',callback_data='search_name_product')
    builder.button(text="Назад",callback_data='main_menu')
    builder.adjust(1)
    return builder.as_markup()

def search_product():
    builder=InlineKeyboardBuilder()
    builder.button(text="Назад",callback_data='search_menu')
    builder.adjust(1)
    return builder.as_markup()

def all_products(products):#Кнопки со всеми доступными ингридиентами
    builder=InlineKeyboardBuilder()
    for id,product_name in products:
        builder.button(text=f'{product_name}',callback_data=filters.MealsWithProduct(action='meal_with_product',product_id=id,product_name=product_name))
    builder.button(text="Назад",callback_data='search_menu')
    builder.adjust(1)
    return builder.as_markup()

def all_meals_with_product(meals,back):#Кнопки со всеми доступными блюдами содержащими в себе заданный ингридиент
    builder=InlineKeyboardBuilder()
    for id,meal in meals:
        builder.button(text=f'{meal}',callback_data=filters.MealsAction(action='info',meal_id=id))
    builder.button(text="Назад",callback_data=back)
    builder.adjust(1)
    return builder.as_markup()

def action_with_meal(meal_id):#Кнопки для добавления блюда в личный кабинет
    builder = InlineKeyboardBuilder()
    builder.button(text="Добавить",callback_data=filters.MealsAction(action='add_to_account',meal_id=meal_id))
    builder.button(text="Назад",callback_data='all_products')
    return builder.as_markup()

def action_complete():
    builder=InlineKeyboardBuilder()
    builder.button(text='Назад',callback_data='all_products')
    builder.button(text='В главное меню',callback_data='main_menu')
    return builder.as_markup()

def search_not_found():
    builder=InlineKeyboardBuilder()
    builder.button(text='Посмотреть все ингридиенты',callback_data='all_products')
    builder.button(text='Назад',callback_data='search_menu')
    builder.adjust(1)
    return builder.as_markup()