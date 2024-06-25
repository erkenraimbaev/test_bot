from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

admin = Router()


@admin.message(Command('admin'))
async def admin_panel(message: Message):
    await message.answer(f'It is admin panel')
