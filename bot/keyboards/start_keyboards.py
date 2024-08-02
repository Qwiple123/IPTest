from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
from enum import Enum




class Action(str, Enum):
    write_message = "write_message"
    look_messages = "look_messages"
    next_page = "next_page"
    previous_page = "previous_page"
    start_menu = "start_menu"
    
    
class StartCallback(CallbackData, prefix="start"):
    action: str
    
class PaginationCallback(CallbackData, prefix="pagination"):
    action: str
    page: int
    
async def start_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text="Написать сообщение",
        callback_data=StartCallback(action="write_message")
    )
    keyboard.button(
        text="Посмотреть сообщения",
        callback_data=StartCallback(action="look_messages")
    )
    return keyboard.as_markup()

async def pagination_keyboard(current_page:int, total_pages:int):
    keyboard = InlineKeyboardBuilder()
    
    if current_page > 1:
        keyboard.button(
            text="Назад", 
            callback_data=PaginationCallback(action="next_page", page=current_page - 1))
    
    if current_page < total_pages:
        keyboard.button(
            text="Далее", 
            callback_data=PaginationCallback(action="previous_page", page=current_page + 1))
    keyboard.button(
            text="Главное меню", 
            callback_data=StartCallback(action="start_menu"))
    
    return keyboard.as_markup()