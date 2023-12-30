import db_requests.requests as db
import keyboards.meals_menu as keyboards
import filters.filters as filters
import captions.captions as captions
from aiogram import types, Router,F

router=Router()
#Меню блюд
@router.callback_query(F.data=='meals_menu')
async def get_all_meals(callback: types.CallbackQuery):
    res=db.get_all_meals()
    
    await callback.message.edit_caption(caption="Все доступные блюда:",reply_markup=keyboards.all_meals(res))
    await callback.answer()

@router.callback_query(filters.MealMenuAction.filter())
async def meal(callback: types.CallbackQuery,callback_data=filters.MealMenuAction):
    meal_id=callback_data.meal_id
    action =callback_data.action

    user_id=callback.from_user.id

    if action=='add_to_account':
        db.add_meal_to_account(user_id,meal_id)
        
        await callback.message.edit_caption(caption="Блюдо добавлено в ваш кабинет",reply_markup=keyboards.action_complete())
    if action=='info_about':
        res=db.get_meal_info(meal_id)
        cap = captions.get_meal_info(res)
        await callback.message.edit_caption(caption=cap,reply_markup=keyboards.menu_meal_action(meal_id))
        
    await callback.answer()
