import sys
import os
import logging
import asyncio
from handlers import account, main_menu,meals_menu,common
from handlers.search import search ,products_catalog,product_search,calories_search,meal_search
from aiogram import Bot, Dispatcher

TOKEN = os.getenv('TG_TOKEN')

async def main() -> None:
    bot = Bot(TOKEN)

    dp = Dispatcher()
    dp.include_routers(
        account.router,
        main_menu.router,
        meals_menu.router,
        common.router,
        search.router,
        products_catalog.router,
        product_search.router,
        calories_search.router,
        meal_search.router
        )

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())