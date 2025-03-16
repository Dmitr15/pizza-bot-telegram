from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from filters.chat_types import ChatTypeFilter
from kbds import reply


user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message:types.Message):
    await message.answer("It was start", reply_markup=reply.start_kb3.as_markup(resize_feyboard=True, input_field_placeholder='What are you interested in?'))



@user_private_router.message((F.text.lower().contains('menu') | (F.text.lower()=='меню')))
@user_private_router.message(Command('menu'))
async def nemu_cmd(message:types.Message):
    await message.answer("Its a menu: ", reply_markup=reply.del_kbd)
    #await message.reply(message.text)

# @user_private_router.message(Command('about'))
# async def nemu_cmd(message:types.Message):
#     await message.answer("About us")

@user_private_router.message((F.text.lower().contains('about us')) | (F.text.lower().contains('about')))
@user_private_router.message(Command('about'))
async def nemu_cmd(message:types.Message):
    await message.answer("About us")

@user_private_router.message((F.text.lower().contains('payment option')) | (F.text.lower().contains('payment')))
@user_private_router.message(Command('payment'))
async def nemu_cmd(message:types.Message):
    await message.answer("Payment options")

@user_private_router.message((F.text.lower().contains('shipping option')) | (F.text.lower().contains('shipping')))
@user_private_router.message(Command('shipping'))
async def nemu_cmd(message:types.Message):
    await message.answer("Shipping options", reply_markup=reply.test_kb)

# @user_private_router.message(F.text.lower().contains('shipping options'))
# async def nemu_cmd(message:types.Message):
#     await message.answer("You are asking about shipping")

@user_private_router.message(F.photo)
async def nemu_cmd(message:types.Message):
    await message.answer("You posted a photo")

# @user_private_router.message(F.text)
# async def nemu_cmd(message:types.Message):
#     await message.answer("You asked something")


@user_private_router.message(F.contact)
async def get_phone(message:types.Message):
    await message.answer(f"Phone was entered")
    await message.answer(str(message.contact))


@user_private_router.message(F.location)
async def get_location(message:types.Message):
    await message.answer(f"Location was entered")
    await message.answer(str(message.location))