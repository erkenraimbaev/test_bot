from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог'),
     KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Контакты')],
    [KeyboardButton(text='Отправить локацию', request_location=True),
     KeyboardButton(text='Отправить контакт', request_contact=True)]
    ], resizekeyboard=True, input_field_placeholder='Выберите пункт меню')


main_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Фрипсы', url='https://google.com'), InlineKeyboardButton(text='Пастила', url='yandex.ru')],
    [InlineKeyboardButton(text='Оплатить', url='stripe.com')]
])
