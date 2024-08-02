from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from environs import Env



env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher(storage=MemoryStorage())