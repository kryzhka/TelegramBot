import keyboards.account as keyboards
import captions.captions as captions
import db_requests.requests as db
from aiogram import types, Router,F
import filters.filters as filters
router=Router()

#Кабинет
@router.callback_query(filters.AccountActionWithAllMeal.filter())
async def send_user_info(callback: types.CallbackQuery,callback_data=filters.AccountActionWithAllMeal):
    
    user_id=callback.from_user.id
    action=callback_data.action
    if action=='delete_all':
        db.delete_all_meals_from_favorites(user_id)
        await callback.message.edit_caption(caption="Блюда удалены из вашего кабинета",reply_markup=keyboards.action_complete())


    user_meals=db.get_user_favorites(user_id)
    info=db.get_sum_of_user_PFC(user_id)

    cap=(
        f"Ваш id: {user_id}\n"
         "Ваши блюда:\n"
        )
    if info['calories'] is not(None):
        cap+=(
            f"Общее количество калорий:{info['calories']}\n"
            f"Общее количество белков:{info['squirrels']}\n"
            f"Общее количество жиров:{info['fats']}\n"
            f"Общее количество углеводов:{info['carbohydrates']}\n"
        )
    await callback.message.edit_caption(caption=cap,reply_markup=keyboards.user_meals(user_meals)) 
    await callback.answer()

@router.callback_query(filters.AccountActionWithMeal.filter())
async def meal(callback: types.CallbackQuery,callback_data=filters.AccountActionWithMeal):
    action =callback_data.action
    meal_id=callback_data.meal_id

    user_id=callback.from_user.id

    if action=='delete':
        db.remove_meal_from_favorites(user_id,meal_id)
        await callback.message.edit_caption(caption="Блюдо удалено из вашего кабинета",reply_markup=keyboards.action_complete())
    if action=='info_about_meal':
        info=db.select_meal(meal_id)
        quantity=db.get_meal_quantity(meal_id)
        cap = captions.get_meal_info(info,quantity)

        await callback.message.edit_caption(caption=cap,reply_markup=keyboards.user_meals_action(meal_id))
    await callback.answer()



