import asyncio
import logging
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message
from aiogram.types.input_file import InputFile

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


# @dp.message(CommandStart())
# async def cmd_start(message: Message):
#     await message.reply('Привет!')
#     await message.answer(text='Hello baby')


@dp.message(CommandStart(deep_link=True, magic=F.args.isdigit()))
async def start_with_link(message: Message, command: CommandObject):
    await message.answer(f'You sended {command.__dict__}')

# @dp.message()
# async def echo(message: Message):
#     await message.answer(text='It is not right!')
#     await message.answer_photo(photo='https://sudoteach.com/static/assets/img/aiogram-banner.jpg',
#                                caption='Лучший курс по aiogram!')


@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID: {message.photo[-1].file_id}')
    print(message.photo[-1].__dict__)


@dp.message(Command('help'))
async def to_help(message: Message):
    await message.reply(f'{message.from_user.first_name} вам нужна помощь?')
    await message.answer(f'Ваш айди: {message.from_user.id}')
    print(message.from_user.__dict__)


@dp.message(Command('photo'))
async def to_help(message: Message):
    await message.answer(f'Ваш photo: {message.from_user.get_profile_photos()}')


@dp.message(Command('get_args'))
async def get_args(message: Message, command: CommandObject):
    if not command.args:
        await message.answer(f'Передайте аргументы!')
    try:
        value1, value2, value3 = command.args.split(' ')
    except Exception:
        await message.answer(f'No')
    else:
        await message.answer(f'There are {value1}, {value2}, {value3}')


@dp.message()
async def echo(message: Message):
    await message.answer(text='It is not right!')
    # await message.answer_photo(photo=aiogram.types.input_file.InputFile('good.jpeg'), caption='Лучший курс по aiogram!')
    # await message.answer_photo(photo=InputFile('good.jpeg'), caption='Bla')
    await message.answer_photo(photo='AgACAgIAAxkBAANQZnmmc5sIGLzxqae6'
                                     '-zmtjHWjdb4AAhbhMRtHdtBLcFiwG680s64BAAMCAAN5AAM1BA', caption='Bla')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f'Exit')
