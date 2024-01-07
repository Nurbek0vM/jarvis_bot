from parsel import Selector
from aiogram import types, Dispatcher
from config import bot
from scraper.new_scraper import NewScraper


async def scraper(call: types.CallbackQuery):
    scrapers = NewScraper()
    links = scrapers.parse_date()
    for link in links[:5]:
        selector = Selector(text=link)
        href_value = selector.css('a::attr(href)').get()
        await bot.send_message(
            chat_id=call.message.chat.id,
            text=href_value
        )


def register_scraper_handler(dp: Dispatcher):
    dp.register_callback_query_handler(
        scraper,
        lambda call: call.data == "scraper_button"
    )