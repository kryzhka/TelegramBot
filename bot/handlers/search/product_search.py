import db_requests.requests as db
import keyboards.search.product_search as keyboards
from aiogram import types, Router,F
from aiogram.fsm.context import FSMContext
from handlers.common import meals_with_product
from filters.filters import ProductNameSearch,InputMessegeProductName,MealsWithProduct
router=Router()

#Поиск ингридиента
@router.callback_query(ProductNameSearch.filter())
async def search_product(callback:types.CallbackQuery,state: FSMContext):
    await state.set_state(InputMessegeProductName.message)
    await state.update_data(data_callback=callback)
    await callback.message.edit_caption(caption="Введите название продукта",reply_markup=keyboards.enter_product_name())
    # await input_profuct_name(message=router.message(F.text))

@router.message(InputMessegeProductName.message)
async def input_product_name(message:types.Message,state: FSMContext):

    input_product_name=message.text
    input_product_name=input_product_name.lower()
    input_product_id=-1
    input_product_id=db.find_products_by_name(input_product_name)['id'][0]
    await message.delete()
    data=await state.get_data()
    if input_product_id==-1:
        await not_found_error(data['data_callback'],state)
    else:
        await meals_with_product(data['data_callback'],MealsWithProduct(product_id=input_product_id,product_name=input_product_name,menu='product_found'))
        await state.clear()

async def not_found_error(callback:types.CallbackQuery,state: FSMContext):
    await callback.message.edit_caption(caption="Продукт не найден",reply_markup=keyboards.search_not_found())
    await state.clear()




