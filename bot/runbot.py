

from loader import dp, bot
from handlers import *
import asyncio

from aiogram.types import BotCommandScopeDefault

async def main():
    await dp.start_polling(bot, skip_updates=False)
    
    

if __name__ == "__main__":
    asyncio.run(main())