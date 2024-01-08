import db_requests.requests as db
import keyboards.search.meal_search as keyboards
from aiogram import types, Router,F
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State,StatesGroup
from filters.filters import MealNameSearch,InputMessegeMealName,FoundedMeals

router=Router()


@router.callback_query(MealNameSearch.filter())
async def meal_name_search(callback: types.CallbackQuery,state:FSMContext):
    await state.set_state(InputMessegeMealName.message)
    await state.update_data(data_callback=callback)
    await callback.message.edit_caption(caption="Введите название блюда",reply_markup=keyboards.search_meal())

@router.message(InputMessegeMealName.message)
async def input_limit_of_calories(message:types.Message,state: FSMContext):
    input_name=message.text
    
    data=await state.get_data()
    await message.delete()
    try:
        await state.update_data(name=input_name)
        await search_results(data['data_callback'],state)
    except:
        await not_found_error(data['data_callback'],state)

@router.callback_query(FoundedMeals.filter())
async def search_results(callback: types.CallbackQuery,state:FSMContext,callback_data=FoundedMeals):
    try:
        data=await state.get_data()
        name=data['name']
    except:
        name=callback_data.name
    meals=db.find_meals_by_name(name)
    await callback.message.edit_caption(caption="Были найдены следующие блюда",reply_markup=keyboards.search_results(meals,name))
    await state.clear()

async def not_found_error(callback: types.CallbackQuery,state:FSMContext):
    await callback.message.edit_caption(caption="Ничего не найдено по заданному пределу",reply_markup=keyboards.search_not_found())
    await state.clear()
