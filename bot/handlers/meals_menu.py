import db_requests.requests as db
import keyboards.meals_menu as keyboards
import filters.meals_menu as filters
import captions.captions as captions
from aiogram import types, Router,F

router=Router()
#Меню блюд
@router.callback_query(F.data=='meals_menu')
async def get_all_meals(callback: types.CallbackQuery):
    res=db.get_all_meals()
    
    await callback.message.edit_caption(caption="Все доступные блюда:",reply_markup=keyboards.all_meals(res))
    await callback.answer()

@router.callback_query(filters.MealInfo.filter())
async def meal(callback: types.CallbackQuery,callback_data=filters.MealInfo):
    meal_id=callback_data.meal_id

    res=db.select_meal(meal_id)
    quantity=db.get_meal_quantity(meal_id)
    cap = captions.get_meal_info(res,quantity)

    await callback.message.edit_caption(caption=cap,reply_markup=keyboards.menu_meal_action(meal_id))
    await callback.answer()

@router.callback_query(filters.AddMealToFavorites.filter())
async def add_meal_to_favorites(callback: types.CallbackQuery,callback_data=filters.AddMealToFavorites):
    meal_id=callback_data.meal_id
    user_id=callback.from_user.id
    db.add_meal_to_favorites(user_id,meal_id)
    await callback.message.edit_caption(caption="Блюдо добавлено в ваш кабинет",reply_markup=keyboards.action_complete())
    await callback.answer()