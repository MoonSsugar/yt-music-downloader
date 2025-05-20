from aiogram import Router, F
from aiogram.types import Message

from keyboards.inline import main_menu

basic_router = Router()

@basic_router.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer(text="Hello", reply_markup=main_menu)
