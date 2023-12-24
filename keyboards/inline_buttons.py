from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_menu_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Начать анкету 🔥",
        callback_data="start_questionnaire"
    )
    registration_button = InlineKeyboardButton(
        "Регистрация 📝",
        callback_data="registration"
    )
    profile_button = InlineKeyboardButton(
        "Мой профил 👤",
        callback_data="my_profile"
    )
    view_profile_button = InlineKeyboardButton(
        "Просмотр профилей 👍🏻👎🏻",
        callback_data="random_profile"
    )
    # ban_users_button = InlineKeyboardButton(
    #     "Забаненные пользователи 🚫",
    #     callback_data="ban_users"
    # )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(profile_button)
    markup.add(view_profile_button)
    # markup.add(ban_users_button)
    return markup


async def start_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    Backend_button = InlineKeyboardButton(
        "Backend 🔥",
        callback_data="Backend"
    )
    FrontEnd_button = InlineKeyboardButton(
        "Front-End 🔥",
        callback_data="Front-End"
    )
    markup.add(Backend_button)
    markup.add(FrontEnd_button)
    return markup


async def direction_backend():
    markup = InlineKeyboardMarkup()
    Python_button = InlineKeyboardButton(
        "Python 🐍",
        callback_data="Python"
    )
    Java_button = InlineKeyboardButton(
        "Java 🔥",
        callback_data="Answer"
    )
    PHP_button = InlineKeyboardButton(
        "PHP 🐘",
        callback_data="Answer"
    )
    markup.add(Python_button)
    markup.add(Java_button)
    markup.add(PHP_button)
    return markup


async def What_frameworks_do_you():
    markup = InlineKeyboardMarkup()
    Django_button = InlineKeyboardButton(
        "Django",
        callback_data="Answer"
    )
    Flask_button = InlineKeyboardButton(
        "Flask",
        callback_data="Answer"
    )
    markup.add(Django_button)
    markup.add(Flask_button)
    return markup


async def direction_FrontEnd():
    markup = InlineKeyboardMarkup()
    JavaScript_button = InlineKeyboardButton(
        "JavaScript",
        callback_data="Answer"
    )
    Angular_button = InlineKeyboardButton(
        "Angular",
        callback_data="Answer"
    )
    Vue_button = InlineKeyboardButton(
        "Vue",
        callback_data="Answer"
    )
    markup.add(JavaScript_button)
    markup.add(Angular_button)
    markup.add(Vue_button)
    return markup


async def like_dislike_keyboard(owner_tg_id):
    markup = InlineKeyboardMarkup()
    python_button = InlineKeyboardButton(
        "LIKE 👍🏻",
        callback_data=f"like_{owner_tg_id}"
    )
    mojo_button = InlineKeyboardButton(
        "DISLIKE 👎🏻",
        callback_data=f"dis_{owner_tg_id}"
    )
    markup.add(python_button)
    markup.add(mojo_button)
    return markup


async def my_profile_keyboard():
    markup = InlineKeyboardMarkup()
    python_button = InlineKeyboardButton(
        "Update 🟢",
        callback_data=f"update_profile"
    )
    mojo_button = InlineKeyboardButton(
        "Delete ❌",
        callback_data="delete_profile"
    )
    markup.add(python_button)
    markup.add(mojo_button)
    return markup

