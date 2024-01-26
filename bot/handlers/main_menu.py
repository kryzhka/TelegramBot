import keyboards.main_menu as keyboards
import db_requests.requests as db

from aiogram import types, Router,F
from aiogram.filters import CommandStart
from aiogram.types import Message , FSInputFile
from filters.filters import MainMenu
router=Router()
#Главное меню
@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user_id=message.from_user.id
    user_name=message.from_user.full_name
    
    db.add_user_to_db(user_id,user_name)
    
    image=FSInputFile("./source/background.png")

    await message.answer_photo(image,caption=f"Здравствуйте, {user_name}",reply_markup=keyboards.main_menu())

@router.callback_query(MainMenu.filter())
async def send_user_info(callback: types.CallbackQuery):
    user_name=callback.from_user.full_name
    await callback.message.edit_caption(caption=f'Здравствуйте, {user_name}',reply_markup=keyboards.main_menu())
    await callback.answer()

# @router.message(F.text)
# async def answer(message:types.Message):
#     await command_start_handler(message)