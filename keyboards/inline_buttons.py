from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_menu_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Начать анкету 🔥",
        callback_data="start_questionnaire"
    )
    markup.add(questionnaire_button)
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