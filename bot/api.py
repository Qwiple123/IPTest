from environs import Env
from aiohttp import ClientSession

env = Env()
env.read_env()

API_URL = env.str("API_URL")

async def fetch_messages(page, per_page) -> list[dict]:
    async with ClientSession() as session:
        async with session.get(f"{API_URL}/messages/?page={page}&per_page={per_page}") as response:
            response.raise_for_status()
            return await response.json()
        
async def post_message(user_id: str, content: str) -> dict:
    async with ClientSession() as session:
        async with session.post(f"{API_URL}/message/", json={"user_id": user_id, "content": content}) as response:
            response.raise_for_status()
            return await response.json()

async def get_user_by_id(user_id:str):
     async with ClientSession() as session:
        async with session.get(f"{API_URL}/users/{user_id}/") as response:
            response.raise_for_status()
            return await response.json()
        
async def get_total_message_count() -> int:
    async with ClientSession() as session:
        async with session.get(f"{API_URL}/messages/count") as response:
            response.raise_for_status()
            count = await response.json()
            return count["total"]