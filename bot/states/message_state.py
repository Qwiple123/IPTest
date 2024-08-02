from aiogram.fsm.state import State, StatesGroup

class Message(StatesGroup):
    write = State()