from environs import Env
from aiogram import BaseMiddleware
from aiogram.types import Message, Update, CallbackQuery
from aiohttp import ClientSession

env = Env()
env.read_env()

API_URL = env.str("API_URL")

class UserExistsMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Update, data: dict):
        user_id = None
        if isinstance(event, Message):
            user_id = event.from_user.id
        elif isinstance(event, CallbackQuery):
            user_id = event.from_user.id

        if user_id:
            async with ClientSession() as session:
                async with session.get(f"{API_URL}/users/{user_id}") as response:
                    if response.status == 404:
                        user_data = {
                            "user_id": user_id,
                            "name": event.from_user.first_name,
                            "nick_name": event.from_user.username,
                        }
                        async with session.post(f"{API_URL}/users/", json=user_data) as create_response:
                            data["user"] = await create_response.json()
                    else:
                        data["user"] = await response.json()
        
        return await handler(event, data)