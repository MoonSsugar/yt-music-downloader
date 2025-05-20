from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Download music",
                             callback_data="music")
    ],
])