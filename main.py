import asyncio
import logging
from aiogram import Dispatcher, Bot

from settings import settings
from handlers.basic import basic_router
from handlers.downloader import downloader_router

logging.basicConfig(level=logging.INFO)

async def main():
    dp = Dispatcher()
    bot = Bot(token=settings.bot_token)
    dp.include_router(basic_router)
    dp.include_router(downloader_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())