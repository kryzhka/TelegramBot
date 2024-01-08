import db_requests.requests as db
from aiogram import types, Router
from filters.filters import GetMealInfo,AddMealToFavorites,MealsWithProduct
import keyboards.account as account_keyboards
import keyboards.meals_menu as meal_menu_keyboards
import keyboards.search.products_catalog as product_catalog_keyboards
import keyboards.search.product_search as product_search_keyboards
import keyboards.search.calories_search as calories_search_keyboards
import keyboards.search.meal_search as meal_name_search
router=Router()

@router.callback_query(GetMealInfo.filter())
async def select_meal(callback: types.CallbackQuery,callback_data=GetMealInfo):
    meal_id=callback_data.meal_id
    menu=callback_data.menu
    product_id=callback_data.product_id
    limit=callback_data.limit
    name=callback_data.name

    info=db.select_meal(meal_id)
    quantity=db.get_meal_quantity(meal_id)
    

    cap=(
    f"Информация о блюде:\n"
    f"Название блюда:\n"
    f"{info['name_meals']}\n"
    f"Количество калорий:     {info['number_of_calories']}\n"
    f"Количество белков:      {info['number_of_squirrels']}\n"
    f"Количество жиров:       {info['number_of_fats']}\n"
    f"Количество углеводов:   {info['number_of_carbohydrates']}\n"
    f"Ингридиенты:\n"
    f"Продукт:        Количество:\n"
    )
    for i in quantity:
        cap+=f"{i[0]}      {i[1]}\n"
    
    if(menu=='favorites'):
        keyboard=account_keyboards.user_meals_action(meal_id)
    elif(menu=='meals_menu'):
        keyboard=meal_menu_keyboards.menu_meal_action(meal_id)
    elif(menu=='found_in_all_products'):
        keyboard=product_catalog_keyboards.action_with_meal(meal_id,product_id)
    elif(menu=='found_in_search_products'):
        keyboard=product_search_keyboards.action_with_meal(meal_id,product_id)
    elif(menu=='calories_search'):
        keyboard=calories_search_keyboards.action_with_meal(meal_id,limit)
    elif(menu=='meal_name_search'):
        keyboard=meal_name_search.action_with_meal(meal_id,name)
    await callback.message.edit_caption(caption=cap,reply_markup=keyboard)
    await callback.answer()

@router.callback_query(AddMealToFavorites.filter())
async def add_meal_to_favorites(callback: types.CallbackQuery,callback_data=AddMealToFavorites):
    meal_id=callback_data.meal_id
    user_id=callback.from_user.id
    menu = callback_data.menu
    product_id=callback_data.product_id
    limit=callback_data.limit
    name=callback_data.name

    db.add_meal_to_favorites(user_id,meal_id)
    if(menu=='meals_menu'):
        keyboard=meal_menu_keyboards.action_complete()
    elif(menu=='found_in_all_products'):
        keyboard=product_catalog_keyboards.action_complete(product_id)
    elif(menu=='found_in_search_products'):
        keyboard=product_search_keyboards.action_complete(product_id)
    elif(menu=='calories_search'):
        keyboard=calories_search_keyboards.action_complete(limit)
    elif(menu=='meal_name_search'):
        keyboard=meal_name_search.action_complete(meal_id,name)
    await callback.message.edit_caption(caption="Блюдо добавлено в ваш кабинет",reply_markup=keyboard)
    await callback.answer()

@router.callback_query(MealsWithProduct.filter())#Вывод всех доступных блюд содержащих в себе заданный ингридиент
async def meals_with_product(callback: types.CallbackQuery,callback_data=MealsWithProduct):
    product_id=callback_data.product_id
    product_name=callback_data.product_name
    menu=callback_data.menu

    res=db.get_meal_with_product(product_id)
    if menu=='all_products':
        keyboard=product_catalog_keyboards.all_meals_with_product(res,product_id)
    elif menu=='product_found':
        keyboard=product_search_keyboards.all_meals_with_product(res,product_id)
    await callback.message.edit_caption(caption=f"Все доступные блюда включающие в себя {product_name}:",reply_markup=keyboard)
    await callback.answer()