import sys
import os
import logging
import asyncio
from handlers import account, main_menu,meals_menu,search_menu,calories_search_menu
from aiogram import Bot, Dispatcher

TOKEN = os.getenv('TG_TOKEN')

async def main() -> None:
    bot = Bot(TOKEN)

    dp = Dispatcher()
    dp.include_routers(account.router, main_menu.router, meals_menu.router, search_menu.router,calories_search_menu.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())