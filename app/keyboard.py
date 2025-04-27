from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

re_cmd = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Rejestracja 📋'),
     KeyboardButton(text='Informacje 📌')]
],
                    resize_keyboard=True)

re_next_reg = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Warsztat 🔧'),
     KeyboardButton(text='Wybierz dostępny dzień 📝')]
],
                    resize_keyboard=True)

in_next_reg = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Wymiana oleju 🪣', callback_data='olej'),
     InlineKeyboardButton(text='Diagnostyka 💻', callback_data='dia')],
    [InlineKeyboardButton(text='Naprawa 🛠', callback_data='rem'),
     InlineKeyboardButton(text='Części zamienne ⚙️', callback_data='mot')]
])

in_next_reg1 = ['Rezerwacja wizyty 👀', 'Zostaw prośbę 💻']

async def in_next_re():
    key_next = InlineKeyboardBuilder()
    for i in in_next_reg1:
        key_next.add(InlineKeyboardButton(text=i, callback_data='callo'))
    return key_next.adjust(2).as_markup()


in_next_dia = ['Rezerwacja wizyty 👀', 'Zostaw prośbę 💻', 'Kontakt 📞']


async def in_diagnos():
    key_dia = InlineKeyboardBuilder()
    for el in in_next_dia:
        key_dia.add(InlineKeyboardButton(text=el, callback_data='dios'))
    return key_dia.adjust(2).as_markup()

in_dia = ['Komputerowa 💻', 'Zawieszenie 🚗', 'Prszed zakupem 👀', 'Umow sie 📅']

async def in_dia_el():
    key = InlineKeyboardBuilder()
    for i in in_dia:
        key.add(InlineKeyboardButton(text=i, callback_data='elektronik'))
    return key.adjust(2).as_markup()


shop = ['Czesci 🔩', 'Sklep ⚜️', 'Kontakt z warsztatem 🏦']

async def in_shop_dia():
    key2 = InlineKeyboardBuilder()
    for i in shop:
        key2.add(InlineKeyboardButton(text=i, callback_data='shop-mech'))
    return key2.adjust(2).as_markup()


re_info = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Rejestracja 📋'),
     KeyboardButton(text='Kontakt 📠')]
],
                    resize_keyboard=True)

re_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='back')]
],
                    resize_keyboard=True)


in_contact = ['Czat intelegencja 🤖', 'Kontakt 📞']

async def in_co():
    keyboard = InlineKeyboardBuilder()
    for el in in_contact:
        keyboard.add(InlineKeyboardButton(text=el, callback_data='krew'))
    return keyboard.adjust(2).as_markup()
