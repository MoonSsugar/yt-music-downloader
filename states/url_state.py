from aiogram.fsm.state import State, StatesGroup

class UrlState(StatesGroup):
    url = State()
