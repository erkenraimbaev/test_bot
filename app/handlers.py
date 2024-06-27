import asyncio

from aiogram import Router
from aiogram.enums import ChatAction
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message
from aiogram import F

router = Router()


@router.message(Command('any'))
async def command_for_channel(message: Message):
    await message.bot.send_dice(chat_id=message.chat.id, emoji='joy')
    # message_thread_id=message.message_thread_id, - если нужно отправить в тред


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id, action=ChatAction.TYPING)
    await message.bot.send_dice(chat_id=message.chat.id, emoji=':joy:')
    await asyncio.sleep(2)
    await message.reply('Привет!')
    await message.answer(text='Hello baby')


# @router.message(CommandStart(deep_link=True, magic=F.args.isdigit()))
# async def start_with_link(message: Message, command: CommandObject):
#     await message.bot.send_chat_action(chat_id=message.from_user.id, action=ChatAction.TYPING)
#     await asyncio.sleep(2)
#     await message.answer(f'You sended {command.__dict__}')

# @router.message()
# async def echo(message: Message):
#     await message.answer(text='It is not right!')
#     await message.answer_photo(photo='https://sudoteach.com/static/assets/img/aiogram-banner.jpg',
#                                caption='Лучший курс по aiogram!')


@router.message(F.document)
async def get_sticker(message: Message):
    await message.answer(f'{message.document.file_id}')


@router.message(F.text == 's')
async def send_sticker(message: Message):
    stickers = ('CAACAgIAAxkBAAEMYKtme8WqZc6JfubiUo6B4BSZUa3qiwACDQADwDZPE6T54fTUeI1TNQQ',
                'CAACAgIAAxkBAAEMYKlme8UIpch10mXVCMo2fO_LkthY-wACAQADwDZPExguczCrPy1RNQQ',
                'CAACAgIAAxkBAAEMYK1me8WyY5HX1rTwhwLbdCtzjlCrxgACCgADwDZPE_8Nrj7oDv0INQQ')
    for stick in stickers:
        await message.answer_sticker(sticker=stick, emoji='😄')


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID: {message.photo[-1].file_id}')
    # print(message.photo[-1].__dict__)


@router.message(Command('help'))
async def to_help(message: Message):
    await message.reply(f'{message.from_user.first_name} вам нужна помощь?')
    await message.answer(f'Ваш айди: {message.from_user.id}')
    print(message.from_user.__dict__)


@router.message(Command('photo'))
async def to_help(message: Message):
    await message.answer(f'Ваш photo: {message.from_user.get_profile_photos()}')


@router.message(Command('get_args'))
async def get_args(message: Message, command: CommandObject):
    if not command.args:
        await message.answer(f'Передайте аргументы!')
    try:
        value1, value2, value3 = command.args.split(' ')
    except Exception:
        await message.answer(f'No')
    else:
        await message.answer(f'There are {value1}, {value2}, {value3}')


@router.message()
async def echo(message: Message):
    await message.answer(text='It is not right!')
    # await message.answer_photo(photo=aiogram.types.input_file.InputFile('good.jpeg'), caption='Лучший курс по
    # aiogram!') await message.answer_photo(photo=InputFile('good.jpeg'), caption='Bla')
    await message.answer_photo(photo='AgACAgIAAxkBAANQZnmmc5sIGLzxqae6'
                                     '-zmtjHWjdb4AAhbhMRtHdtBLcFiwG680s64BAAMCAAN5AAM1BA', caption='Bla')
