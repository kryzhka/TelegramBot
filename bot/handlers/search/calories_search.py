import keyboards.search.calories_search as keyboards
import db_requests.requests as db
from aiogram import types, Router,F
from filters.filters import CaloriesSearch,InputMessegeLimit,MealsWithCalories
from aiogram.fsm.context import FSMContext
router=Router()

@router.callback_query(CaloriesSearch.filter())
async def calories_search_menu(callback: types.CallbackQuery,state:FSMContext):
    await state.set_state(InputMessegeLimit.message)
    await state.update_data(data_callback=callback)
    await callback.message.edit_caption(caption="Введите верхний предел калорий блюда",reply_markup=keyboards.search_product())

@router.message(InputMessegeLimit.message)
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

@router.callback_query(MealsWithCalories.filter())
async def search_results(callback: types.CallbackQuery,state:FSMContext,callback_data=MealsWithCalories):
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

