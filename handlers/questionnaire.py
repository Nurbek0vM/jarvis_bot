import sqlite3

from aiogram import types, Dispatcher
from config import bot
from keyboards import inline_buttons


async def start_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Python🐍 or Mojo🔥",
        reply_markup=await inline_buttons.start_questionnaire_keyboard()
    )

async def start_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Какая направления тебе нравится 🧐",
        reply_markup=await inline_buttons.start_questionnaire_keyboard()
    )

async def direction_backend_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Какая язык программирования тебе нравится",
        reply_markup=await inline_buttons.direction_backend()
    )

async def direction_FrontEnd_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Какая язык программирования тебе нравится",
        reply_markup=await inline_buttons.direction_FrontEnd()
    )

async def Python_language_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Какие фреймворки ты предпочитаешь?",
        reply_markup=await inline_buttons.What_frameworks_do_you()
    )

async def Answer_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Хороший выбор 👍",
    )

def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(direction_backend_call,
                                       lambda call: call.data == "Backend")
    dp.register_callback_query_handler(direction_FrontEnd_call,
                                       lambda call: call.data == "Front-End")
    dp.register_callback_query_handler(Python_language_call,
                                       lambda call: call.data == "Python")
    dp.register_callback_query_handler(Answer_call,
                                       lambda call: call.data == "Answer")

