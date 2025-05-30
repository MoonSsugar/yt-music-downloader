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
    if os.path.exists(f"{call.from_user.id}"):
        pass
    else:
        os.mkdir(f"{call.from_user.id}")
    await state.set_state(UrlState.url)
    await call.message.answer(text="Send url.")
    await call.answer()

@downloader_router.message(StateFilter(UrlState.url))
async def downloader(message: Message, state: FSMContext):
    await state.set_data({"url": message.text})
    data = await state.get_data()
    url = data["url"]
    counter = 0
    await download(url=url, id=str(message.from_user.id))
    for file in os.listdir(f"{message.from_user.id}\\"):
        if ".m4a" not in file:
            continue
        await message.answer_audio(FSInputFile(path=f"{message.from_user.id}\\{file}"))
        os.remove(f"{message.from_user.id}\\{file}")
        counter+=1
    await state.clear()
    await message.answer(text=f"{counter}")
    await message.answer(text="Anything else?", reply_markup=main_menu)
