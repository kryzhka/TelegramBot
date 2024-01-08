from aiogram.utils.keyboard import InlineKeyboardBuilder
from filters.filters import MainMenu,ProductSearch,GetAllProducts,MealsWithProduct,GetMealInfo,AddMealToFavorites

#Поиск

#Поиск блюда по всем ингридиентам
def all_products(products):#Кнопки со всеми доступными ингридиентами
    builder=InlineKeyboardBuilder()
    for id,product_name in products:
        builder.button(text=f'{product_name}',callback_data=MealsWithProduct(product_id=id,product_name=product_name,menu='all_products'))
    builder.button(text="Назад",callback_data=ProductSearch())
    builder.adjust(1)
    return builder.as_markup()

def all_meals_with_product(meals,product_id):#Кнопки со всеми доступными блюдами содержащими в себе заданный ингридиент
    builder=InlineKeyboardBuilder()
    for id,meal in meals:
        builder.button(text=f'{meal}',callback_data=GetMealInfo(meal_id=id,product_id=product_id,menu='found_in_all_products'))
    builder.button(text="Назад",callback_data=GetAllProducts())
    builder.adjust(1)
    return builder.as_markup()

def action_with_meal(meal_id,product_id):#Кнопки для добавления блюда в личный кабинет
    builder = InlineKeyboardBuilder()
    builder.button(text="Добавить",callback_data=AddMealToFavorites(meal_id=meal_id,menu='found_in_all_products',product_id=product_id))
    builder.button(text="Назад",callback_data=MealsWithProduct(product_id=product_id,product_name=' ',menu='all_products'))
    return builder.as_markup()

def action_complete(product_id):
    builder=InlineKeyboardBuilder()
    builder.button(text='Назад',callback_data=GetAllProducts())
    builder.button(text='В главное меню',callback_data=MealsWithProduct(product_id=product_id,product_name=' ',menu='all_products'))
    return builder.as_markup()