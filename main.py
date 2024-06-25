import asyncio
import logging
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F

from app.admin import admin
from app.handlers import router


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_routers(router, admin)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f'Exit')
