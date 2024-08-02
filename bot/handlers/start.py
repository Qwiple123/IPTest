from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiohttp import ClientSession
from loader import dp, bot
from keyboards.start_keyboards import start_keyboard, pagination_keyboard
from utils.set_bot_commands import set_default_commands
from keyboards.start_keyboards import StartCallback, Action, PaginationCallback
from states.message_state import Message
from aiogram.fsm.context import FSMContext
from api import fetch_messages, post_message, get_user_by_id, get_total_message_count
from middleware.user_exist import UserExistsMiddleware
from datetime import datetime




MESSAGES_PER_PAGE = 10

dp.message.middleware(UserExistsMiddleware())
dp.callback_query.middleware(UserExistsMiddleware())


@dp.message(Command(commands=["start"]))
async def start_message(message: types.Message, user: dict):
    await set_default_commands(bot)
    await message.answer(f"Привет {user['nick_name']}\n Я бот для работы с сообщениями", reply_markup=await start_keyboard())
    
@dp.callback_query(StartCallback.filter(F.action == Action.start_menu))
async def start_message_query(query: types.CallbackQuery, user: dict):
    await query.answer()
    await query.message.delete()
    await query.message.answer(f"Привет {user['nick_name']}\n Я бот для работы с сообщениями", reply_markup=await start_keyboard())
    
    
@dp.callback_query(StartCallback.filter(F.action == Action.write_message))
async def write_message(query: types.CallbackQuery, state: FSMContext, user: dict):
    await query.answer()
    await query.message.delete()
    await state.set_state(Message.write)
    message = await query.message.answer("Привет напиши свое сообщение и оно отправится")
    await state.set_data({"message":message})
    
@dp.message(Message.write)
async def write_message_finish(message: types.Message, state: FSMContext, user: dict):
    data = await state.get_data()
    msg = data["message"]
    await msg.delete()
    await state.clear()
    await post_message(user["user_id"], message.text)
    await message.answer("Ваше сообщение было отправлено")
    await start_message(message, user)
    
@dp.callback_query(StartCallback.filter(F.action == Action.look_messages))
@dp.callback_query(PaginationCallback.filter(F.action == Action.next_page))
@dp.callback_query(PaginationCallback.filter(F.action == Action.previous_page))
async def look_messages(query: types.CallbackQuery, callback_data: dict, user:dict):
    await query.answer()
    if callback_data.action == "look_messages":
        page = 1
    else:
        page = callback_data.page
    messages = await fetch_messages(page, MESSAGES_PER_PAGE)
    if not messages:
        await query.message.edit_text(f"Сейчас сообщений нет")
        return
    answer_string = f"Страница №{page}\n"
    
    
    for message in messages:
        user = await get_user_by_id(message["user_id"])
        date = datetime.fromisoformat(message['created_at'])
        formatted_date = date.strftime("%Y-%m-%d %H:%M:%S")
        answer_string += f"[{user['nick_name']}] {message['content']} - {formatted_date} \n\n"
        
    total_messages = await get_total_message_count()
    total_pages = (total_messages + MESSAGES_PER_PAGE - 1) // MESSAGES_PER_PAGE
    
    await query.message.edit_text(f"{answer_string}")
    await query.message.edit_reply_markup(reply_markup=await pagination_keyboard(page, total_pages))
    
    
