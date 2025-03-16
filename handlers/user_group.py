from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from string import punctuation
from filters.chat_types import ChatTypeFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))

restricted_words = {'cat', 'dog', 'pig'}


def clear_txt(txt: str):
    return txt.translate(str.maketrans('', '', punctuation))


# @user_group_router.message()
# async def cleaner(message: types.Message):
#     if restricted_words.intersection(message.text.lower().split()):
#         await message.answer(f'{message.from_user.first_name}, follow the community rules!')
#         await message.delete()

@user_group_router.edited_message()
@user_group_router.message()
async def cleaner(message: types.Message):
    if restricted_words.intersection(clear_txt(message.text.lower()).split()):
        await message.answer(f"{message.from_user.first_name}, соблюддайте порядок в чате!")
        await message.delete()