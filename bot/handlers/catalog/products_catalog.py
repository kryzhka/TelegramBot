import db_requests.requests as db
import keyboards.catalog.products_catalog as keyboards
from aiogram import types, Router
from filters.filters import ProductCatalog,CatalogMealsWithProduct
router=Router()

#Все ингридиенты
@router.callback_query(ProductCatalog.filter())#Вывод всех доступных ингридиентов
async def all_products(callback: types.CallbackQuery):
    res=db.get_all_products()
    print(res)
    await callback.message.edit_caption(caption="Все доступные ингридиенты:",reply_markup=keyboards.all_products(res))
    await callback.answer()

@router.callback_query(CatalogMealsWithProduct.filter())#Вывод всех доступных блюд содержащих в себе заданный ингридиент
async def meals_with_product(callback: types.CallbackQuery,callback_data=CatalogMealsWithProduct):
    product_id=callback_data.product_id
    res=db.get_meal_with_product(product_id)

   
    await callback.message.edit_caption(caption=f"Блюда содержащие, данный ингридиент:",reply_markup= keyboards.all_meals_with_product(res,product_id))
    await callback.answer()