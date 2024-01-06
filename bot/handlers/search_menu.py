import db_requests.requests as db
import keyboards.search_menu as keyboards
import filters.filters as filters
import captions.captions as captions
from aiogram import types, Router,F
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State,StatesGroup
router=Router()

#Поиск по ингридиенту
@router.callback_query(F.data=='search_menu')
async def search_menu(callback: types.CallbackQuery):
    await callback.message.edit_caption(caption="",reply_markup=keyboards.search_menu())

@router.callback_query(F.data=='search_name_product')
async def search_product(callback:types.CallbackQuery,state: FSMContext):
    await state.set_state(filters.InputMessege.message)
    await state.update_data(data_callback=callback)
    await callback.message.edit_caption(caption="Введите название продукта",reply_markup=keyboards.search_product())
    # await input_profuct_name(message=router.message(F.text))

@router.message(filters.InputMessege.message)
async def input_profuct_name(message:types.Message,state: FSMContext):

    input_product_name=message.text
    input_product_name=input_product_name.lower()
    input_product_id=-1
    products=db.get_all_products()
    for id,product_name in products:
        if input_product_name==product_name.lower():
            input_product_id=id
    await message.delete()
    data=await state.get_data()
    if input_product_id==-1:
        await not_found_error(data['data_callback'],state)
    else:
        await meals_with_product(data['data_callback'],filters.MealsWithProduct(action='meal_with_product',product_id=input_product_id,product_name=input_product_name),back='search_menu')
        await state.clear()

async def not_found_error(callback:types.CallbackQuery,state: FSMContext):
    await callback.message.edit_caption(caption="Продукт не найден",reply_markup=keyboards.search_not_found())
    await state.clear()


@router.callback_query(F.data=='all_products')#Вывод всех доступных ингридиентов
async def all_products(callback: types.CallbackQuery):
    res=db.get_all_products()
    await callback.message.edit_caption(caption="Все доступные ингридиенты:",reply_markup=keyboards.all_products(res))

@router.callback_query(filters.MealsWithProduct.filter())#Вывод всех доступных блюд содержащих в себе заданный ингридиент
async def meals_with_product(callback: types.CallbackQuery,callback_data=filters.MealsWithProduct,back='all_products'):
    product_id=callback_data.product_id
    product_name=callback_data.product_name
    action=callback_data.action
    if action=="meal_with_product":
        res=db.get_meal_with_product(product_id)
        await callback.message.edit_caption(caption=f"Все доступные блюда с ингридиентом {product_name}:",reply_markup=keyboards.all_meals_with_product(res,back))
    await callback.answer()

@router.callback_query(filters.MealsAction.filter())#Вывод информации о выбранном блюде и возможность его добавить в личный кабинет
async def meal_with_product(callback: types.CallbackQuery,callback_data=filters.MealsAction):
    meal_id=callback_data.meal_id
    action=callback_data.action

    user_id=callback.from_user.id
    if action=="info":
        res=db.select_meal(meal_id)
        quantity=db.get_meal_quantity(meal_id)
        cap = captions.get_meal_info(res,quantity)
        await callback.message.edit_caption(caption=cap,reply_markup=keyboards.action_with_meal(meal_id))
    if action == "add_to_account":
        db.add_meal_to_favorites(user_id,meal_id)
        await callback.message.edit_caption(caption="Блюдо добавлено в ваш кабинет",reply_markup=keyboards.action_complete())
    await callback.answer()

