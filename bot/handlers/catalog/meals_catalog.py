import db_requests.requests as db
import keyboards.catalog.meals_catalog as keyboards
from filters.filters import MealCatalog,GetMealInfo,AddMealToFavorites
from aiogram import types, Router,F

router=Router()
#Меню блюд
@router.callback_query(MealCatalog.filter())
async def get_all_meals(callback: types.CallbackQuery):
    res=db.get_all_meals()
    
    await callback.message.edit_caption(caption="Все доступные блюда:",reply_markup=keyboards.all_meals(res))
    await callback.answer()
