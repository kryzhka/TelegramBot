import db_requests.requests as db
import keyboards.catalog.catalog as keyboards
from filters.filters import Catalog
from aiogram import types, Router,F

router=Router()
#Меню блюд
@router.callback_query(Catalog.filter())
async def get_all_meals(callback: types.CallbackQuery):
    
    await callback.message.edit_caption(caption="Выберите каталог: ",reply_markup=keyboards.chose_catalog())
    await callback.answer()