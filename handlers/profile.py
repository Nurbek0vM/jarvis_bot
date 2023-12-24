import re
import sqlite3

from aiogram import types, Dispatcher
from config import bot, ADMIN_ID
from const import PROFILE_TEXT
from database.sql_commands import Database
import random

from keyboards.inline_buttons import like_dislike_keyboard, my_profile_keyboard


async def my_profile_call(call: types.CallbackQuery):
    db = Database()
    profile = db.sql_select_profile(
        tg_id=call.from_user.id
    )
    if profile:
        with open(profile['photo'], 'rb') as photo:
            await bot.send_photo(
                chat_id=call.from_user.id,
                photo=photo,
                caption=PROFILE_TEXT.format(
                    nickname=profile['nickname'],
                    biography=profile['biography'],
                    age=profile['age'],
                    gender=profile['gender'],
                    favorite_color=profile['favorite_color'],
                    citizenshipe=profile['citizenshipe']
                ),
                parse_mode=types.ParseMode.MARKDOWN,
                reply_markup=await my_profile_keyboard()
            )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text='У вас нет профиля, пожалуйста, зарегистрируйтесь'
        )


async def random_profile_like_call(call: types.CallbackQuery):
    db = Database()
    profiles = db.sql_select_filter_like_profiles(
        tg_id=call.from_user.id
    )
    if profiles:
        random_profile = random.choice(profiles)
        with open(random_profile['photo'], 'rb') as photo:
            await bot.send_photo(
                chat_id=call.from_user.id,
                photo=photo,
                caption=PROFILE_TEXT.format(
                    nickname=random_profile['nickname'],
                    biography=random_profile['biography'],
                    age=random_profile['age'],
                    gender=random_profile['gender'],
                    favorite_color=random_profile['favorite_color'],
                    citizenshipe=random_profile['citizenshipe']
                ),
                parse_mode=types.ParseMode.MARKDOWN,
                reply_markup=await like_dislike_keyboard(owner_tg_id=random_profile['telegram_id'])
            )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text='Нет профилей, которые вам не понравились'
        )

async def like_detect_call(call: types.CallbackQuery):
    db = Database()
    owner = re.sub("like_", "", call.data)
    print(call.data)
    print(owner)
    try:
        db.sql_insert_like(
            owner=owner,
            liker=call.from_user.id
        )
    except sqlite3.IntegrityError:
        await bot.send_message(
            chat_id=call.from_user.id,
            text='Тебе нравился этот профиль раньше'
        )
    finally:
        await random_profile_like_call(call=call)

async def random_profile_dislike_call(call: types.CallbackQuery):
    db = Database()
    profiles = db.sql_select_filter_dislike_profiles(
        tg_id=call.from_user.id
    )
    if profiles:
        random_profile = random.choice(profiles)
        with open(random_profile['photo'], 'rb') as photo:
            await bot.send_photo(
                chat_id=call.from_user.id,
                photo=photo,
                caption=PROFILE_TEXT.format(
                    nickname=random_profile['nickname'],
                    biography=random_profile['biography'],
                    age=random_profile['age'],
                    gender=random_profile['gender'],
                    favorite_color=random_profile['favorite_color'],
                    citizenshipe=random_profile['citizenshipe']
                ),
                parse_mode=types.ParseMode.MARKDOWN,
                reply_markup=await like_dislike_keyboard(owner_tg_id=random_profile['telegram_id'])
            )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text='Нет профилей, которые вам понравилось'
        )

async def dislike_detect_call(call: types.CallbackQuery):
    db = Database()
    owner = re.sub("dis_", "", call.data)
    print(call.data)
    print(owner)
    try:
        db.sql_insert_dislike(
            owner=owner,
            disliker=call.from_user.id
        )
    except sqlite3.IntegrityError:
        await bot.send_message(
            chat_id=call.from_user.id,
            text='Тебе ненравился этот профиль раньше'
        )
    finally:
        await random_profile_dislike_call(call=call)

async def delete_profile_call(call: types.CallbackQuery):
    db = Database()
    db.sql_delete_profile(
        tg_id=call.from_user.id
    )
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Профиль успешно удален'
    )


def register_profile_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        my_profile_call,
        lambda call: call.data == 'my_profile'
    )
    dp.register_callback_query_handler(
        random_profile_like_call,
        lambda call: call.data == 'random_profile'
    )
    dp.register_callback_query_handler(
        random_profile_dislike_call,
        lambda call: call.data == 'random_profile'
    )
    dp.register_callback_query_handler(
        delete_profile_call,
        lambda call: call.data == 'delete_profile'
    )
    dp.register_callback_query_handler(
        like_detect_call,
        lambda call: "like_" in call.data
    )
    dp.register_callback_query_handler(
        dislike_detect_call,
        lambda call: "dis_" in call.data
    )