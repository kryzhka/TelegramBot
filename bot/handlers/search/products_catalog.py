import db_requests.requests as db
import keyboards.search.products_catalog as keyboards
from aiogram import types, Router
from filters.filters import GetAllProducts
router=Router()

#Все ингридиенты
@router.callback_query(GetAllProducts.filter())#Вывод всех доступных ингридиентов
async def all_products(callback: types.CallbackQuery):
    res=db.get_all_products()
    await callback.message.edit_caption(caption="Все доступные ингридиенты:",reply_markup=keyboards.all_products(res))
    await callback.answer()

