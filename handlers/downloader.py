import os
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from states.url_state import UrlState
from service.yt_downloader import download
from keyboards.inline import main_menu

downloader_router = Router()

@downloader_router.callback_query(F.data == "music")
async def get_url(call: CallbackQuery, state: FSMContext):
    await state.set_state(UrlState.url)
    await call.message.answer(text="Wait a minute, your musuc is downloading...")
    await call.answer()

@downloader_router.message(StateFilter(UrlState.url))
async def downloader(message: Message, state: FSMContext):
    await state.set_data({"url": message.text})
    data = await state.get_data()
    url = data["url"]
    await download(url=url)
    for file in os.listdir("."):
        if ".m4a" not in file:
            continue
        await message.answer_document(FSInputFile(file))
        os.remove(file)
    await state.clear()
    await message.answer(text="Anything else?", reply_markup=main_menu)
