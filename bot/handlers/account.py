import keyboards.account as keyboards
import db_requests.requests as db
from aiogram import F,types, Router
from filters.filters import Favorites,DeleteAllFromFavorites,GetMealInfo,DeleteFromFavorites
router=Router()

#Кабинет
@router.callback_query(Favorites.filter())
async def get_user_favorites(callback: types.CallbackQuery):
    
    user_id=callback.from_user.id
    user_meals=db.get_user_favorites(user_id)
    info=db.get_sum_of_user_PFC(user_id)

    cap=(
        f"Ваш id: {user_id}\n"
        )
    if info['calories'] is not(None):
        cap+=(
            f"Общее количество калорий:{info['calories']}\n"
            f"Общее количество белков:{info['squirrels']}\n"
            f"Общее количество жиров:{info['fats']}\n"
            f"Общее количество углеводов:{info['carbohydrates']}\n"
            f"Ваши блюда:\n"
        )
    await callback.message.edit_caption(caption=cap,reply_markup=keyboards.user_meals(user_meals)) 
    await callback.answer()

@router.callback_query(DeleteAllFromFavorites.filter())
async def delete_all_favorites(callback: types.CallbackQuery):
    user_id=callback.from_user.id
    db.delete_all_meals_from_favorites(user_id)
    await callback.message.edit_caption(caption="Блюда удалены из вашего кабинета",reply_markup=keyboards.action_complete())
    await callback.answer()

@router.callback_query(DeleteFromFavorites.filter())
async def delete_meal_from_favorites(callback: types.CallbackQuery,callback_data=DeleteFromFavorites):
    user_id=callback.from_user.id
    meal_id=callback_data.meal_id
    db.remove_meal_from_favorites(user_id,meal_id)
    await callback.message.edit_caption(caption="Блюдо удалено из вашего кабинета",reply_markup=keyboards.action_complete())
    await callback.answer()
