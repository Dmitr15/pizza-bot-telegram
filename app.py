import os

from aiogram.types import BotCommandScopeAllPrivateChats
from dotenv import load_dotenv
from common.bot_cmds_list import private

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from handlers.user_private import user_private_router
from handlers.user_group import user_group_router

load_dotenv()
ALLOWED_UPDATES = ['message', 'edited_message']

PIZZA_BOT_TOKEN = os.getenv('PIZZA_BOT_TOKEN')

bot = Bot(token=PIZZA_BOT_TOKEN)

dp = Dispatcher()

dp.include_router(user_private_router)
dp.include_router(user_group_router)


# @dp.message(CommandStart())
# async def start_cmd(message:types.Message):
#     await message.answer('It was start')
#
#
# @dp.message()
# async def echo(message:types.Message, bot:Bot):
#     #await bot.send_message(message.from_user.id, 'Answer')
#     await message.answer(message.text)
#     #await message.reply(message.text)


# @dp.message()
# async def echo(message:types.Message):
#     text: str | None = message.text
#     hellolist = ['Hi', 'Hello', 'Привет', 'hi', 'привет', 'hello']
#     byelist = ['Bye', 'bye', 'Goodbye']
#
#     if any(elem in text for elem in hellolist):
#         await message.answer('Nice to see you again!')
#     elif any(elem in text for elem in byelist):
#         await message.answer('Goodbye!')
#     else:
#         await message.answer(message.text)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=['message', 'edited_message'])


asyncio.run(main())
