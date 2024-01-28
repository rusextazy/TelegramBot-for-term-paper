from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_menu = [
    [KeyboardButton(text="☕️ Связаться с нами")],
    [KeyboardButton(text="👨‍💻 Подача заявления на обучение")]
]

kb_menu = ReplyKeyboardMarkup(keyboard=kb_menu, resize_keyboard=True)

kb_exit = [
    [KeyboardButton(text="🔙 Главное меню")]
]

kb_exit = ReplyKeyboardMarkup(keyboard=kb_exit, resize_keyboard=True)
