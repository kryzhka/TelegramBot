import keyboards.calories_search_menu as keyboards
import captions.captions as captions
import db_requests.requests as db
from aiogram import types, Router,F
import filters.filters as filters
from aiogram.fsm.context import FSMContext
router=Router()

@router.callback_query(F.data=='calories_search_menu')
async def calories_search_menu(callback: types.CallbackQuery,state:FSMContext):
    await state.set_state(filters.InputMessegeLimit.message)
    await state.update_data(data_callback=callback)
    await callback.message.edit_caption(caption="Введите верхний предел калорий блюда",reply_markup=keyboards.search_product())

@router.message(filters.InputMessegeLimit.message)
async def input_limit_of_calories(message:types.Message,state: FSMContext):
    input_limit=message.text
    
    data=await state.get_data()
    await message.delete()
    try:
        input_limit=int(input_limit)
        await state.update_data(limit=input_limit)
        await search_results(data['data_callback'],state)
    except:
        await not_found_error(data['data_callback'],state)
@router.callback_query(filters.MealsWithCalories.filter())
async def search_results(callback: types.CallbackQuery,state:FSMContext,callback_data=filters.MealsWithCalories):
    try:
        data=await state.get_data()
        limit=data['limit']
    except:
        limit=callback_data.limit
    meals=db.get_meals_with_limit(limit)
    await callback.message.edit_caption(caption="Были найдены следующие блюда",reply_markup=keyboards.search_results(meals,limit))
    await state.clear()

async def not_found_error(callback: types.CallbackQuery,state:FSMContext):
    await callback.message.edit_caption(caption="Ничего не найдено по заданному пределу",reply_markup=keyboards.search_not_found())
    await state.clear()

@router.callback_query(filters.MealsActionCaloriesMenu.filter())#Вывод информации о выбранном блюде и возможность его добавить в личный кабинет
async def meal_with_product(callback: types.CallbackQuery,callback_data=filters.MealsActionCaloriesMenu):
    meal_id=callback_data.meal_id
    action=callback_data.action

    user_id=callback.from_user.id
    if action=="info":
        res=db.select_meal(meal_id)
        quantity=db.get_meal_quantity(meal_id)
        cap = captions.get_meal_info(res,quantity)
        await callback.message.edit_caption(caption=cap,reply_markup=keyboards.action_with_meal(meal_id,callback_data.limit))
    if action == "add_to_account":
        db.add_meal_to_favorites(user_id,meal_id)
        await callback.message.edit_caption(caption="Блюдо добавлено в ваш кабинет",reply_markup=keyboards.action_complete(callback_data.limit))
    await callback.answer()