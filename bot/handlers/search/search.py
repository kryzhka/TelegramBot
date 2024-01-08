from aiogram import types, Router
from filters.filters import Search,ProductSearch
import keyboards.search.search as keyboards
router=Router()
@router.callback_query(Search.filter())
async def search_menu(callback: types.CallbackQuery):
    await callback.message.edit_caption(caption="",reply_markup=keyboards.search_menu())

#Меню поиска по ингридиенту
@router.callback_query(ProductSearch.filter())
async def search_menu(callback: types.CallbackQuery):
    await callback.message.edit_caption(caption="",reply_markup=keyboards.product_search_menu())