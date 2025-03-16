from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Menu'),
            KeyboardButton(text='About'),
        ],
        [
            KeyboardButton(text='Shipping options'),
            KeyboardButton(text='Payment options'),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='What are you interested in'
)

del_kbd = ReplyKeyboardRemove()

start_kb2 = ReplyKeyboardBuilder()
start_kb2.add(
    KeyboardButton(text='Menu'),
    KeyboardButton(text='About'),
    KeyboardButton(text='Shipping options'),
    KeyboardButton(text='Payment options'),
)
start_kb2.adjust(2, 2)

start_kb3 = ReplyKeyboardBuilder()
start_kb3.attach(start_kb2)
start_kb3.row(KeyboardButton(text='Write a comment'))
# start_kb3.adjust(2, 2)

test_kb=ReplyKeyboardMarkup(
keyboard=[
        [
            KeyboardButton(text='Open pool', request_poll=KeyboardButtonPollType()),
        ],
        [
            KeyboardButton(text='Enter phone', request_contact=True),
            KeyboardButton(text='Enter location', request_location=True),
        ],
    ],


)