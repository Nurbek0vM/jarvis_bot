import sqlite3

from aiogram import types, Dispatcher
from config import bot, MEDIA_DESTINATION
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from const import PROFILE_TEXT
from database.sql_commands import Database


class RegistrationStates(StatesGroup):
    nickname = State()
    biography = State()
    age = State()
    gender = State()
    favorite_color = State()
    citizenshipe = State()
    photo = State()


async def start_registration(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Отправьте мне свое имя, пожалуйста ?"
    )
    await RegistrationStates.nickname.set()


async def update_profile_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Отправьте мне свое имя, пожалуйста ?'
    )
    await RegistrationStates.nickname.set()


async def load_nickname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Расскажи о себе ?"
    )
    await RegistrationStates.next()


async def load_biography(message: types.Message,
                         state: FSMContext):
    async with state.proxy() as data:
        data['biography'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Сколько тебе лет?\n"
             "Отправьте мне только числовой ответ!\n"
             "Пример: 18, 20, 25\n"
             "Не хорошо: Двадцать, Семнадцать."
    )
    await RegistrationStates.next()


async def load_age(message: types.Message,
                   state: FSMContext):
    try:
        type(int(message.text))
    except ValueError:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Я сказал, пришлите мне только числовой ответ\n"
                 "Зарегистрируйтесь, ваша регистрация завершена!!"
        )
        await state.finish()
        return

    async with state.proxy() as data:
        data['age'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Отправь мне свой пол"
    )
    await RegistrationStates.next()


async def load_gender(message: types.Message,
                      state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Любимый цвет?"
    )
    await RegistrationStates.next()


async def load_favorite_color(message: types.Message,
                              state: FSMContext):
    async with state.proxy() as data:
        data['favorite_color'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Гражданство?"
    )
    await RegistrationStates.next()


async def load_citizenshipe(message: types.Message,
                           state: FSMContext):
    async with state.proxy() as data:
        data['citizenshipe'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Отправь мне свое фото 📸"
    )
    await RegistrationStates.next()


async def load_photo(message: types.Message,
                     state: FSMContext):
    db = Database()
    print(message.photo)
    path = await message.photo[-1].download(
        destination_dir=MEDIA_DESTINATION
    )
    print(path.name)
    profile = db.sql_select_profile(
        tg_id=message.from_user.id
    )
    async with state.proxy() as data:
        if not profile:
            db.sql_insert_profile(
                tg_id=message.from_user.id,
                nickname=data['nickname'],
                biography=data['biography'],
                age=data['age'],
                gender=data['gender'],
                favorite_color=data['favorite_color'],
                citizenshipe=data['citizenshipe'],
                photo=path.name
            )
            await bot.send_message(
                chat_id=message.from_user.id,
                text="Вы успешно зарегистрировались 👍"
            )
        elif profile:
            db.sql_update_profile(
                nickname=data['nickname'],
                biography=data['biography'],
                age=data['age'],
                gender=data['gender'],
                favorite_color=data['favorite_color'],
                citizenshipe=data['citizenshipe'],
                photo=path.name,
                tg_id=message.from_user.id
            )
            await bot.send_message(
                chat_id=message.from_user.id,
                text="Вы успешно зарегистрировались 👍"
            )
        with open(path.name, 'rb') as photo:
            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=photo,
                caption=PROFILE_TEXT.format(
                    nickname=data['nickname'],
                    biography=data['biography'],
                    age=data['age'],
                    gender=data['gender'],
                    favorite_color=data['favorite_color'],
                    citizenshipe=data['citizenshipe']
                ),
            )
        await state.finish()


def registration_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        start_registration,
        lambda call: call.data == "registration"
    )
    dp.register_callback_query_handler(
        update_profile_call,
        lambda call: call.data == "update_profile"
    )
    dp.register_message_handler(
        load_nickname,
        state=RegistrationStates.nickname,
        content_types=['text']
    )

    dp.register_message_handler(
        load_biography,
        state=RegistrationStates.biography,
        content_types=['text']
    )

    dp.register_message_handler(
        load_age,
        state=RegistrationStates.age,
        content_types=['text']
    )

    dp.register_message_handler(
        load_gender,
        state=RegistrationStates.gender,
        content_types=['text']
    )

    dp.register_message_handler(
        load_favorite_color,
        state=RegistrationStates.favorite_color,
        content_types=['text']
    )

    dp.register_message_handler(
        load_citizenshipe,
        state=RegistrationStates.citizenshipe,
        content_types=['text']
    )

    dp.register_message_handler(
        load_photo,
        state=RegistrationStates.photo,
        content_types=types.ContentTypes.PHOTO
    )