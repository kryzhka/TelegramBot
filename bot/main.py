import sys
import os
import logging
import asyncio
from handlers import account, main_menu,common
from handlers.search import search,product_search,calories_search,meal_search
from handlers.catalog import meals_catalog,products_catalog,catalog
from aiogram import Bot, Dispatcher

TOKEN = os.getenv('TG_TOKEN')

async def main() -> None:
    bot = Bot(TOKEN)

    dp = Dispatcher()
    dp.include_routers(
        account.router,
        main_menu.router,
        common.router,
        search.router,
        catalog.router,
        products_catalog.router,
        meals_catalog.router,
        product_search.router,
        calories_search.router,
        meal_search.router
        )

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())