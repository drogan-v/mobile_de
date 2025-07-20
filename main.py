import logging
import os

from dotenv import load_dotenv
from telegram import Update, MessageEntity
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

from src.mobile_de import MobileDe

load_dotenv(verbose=True)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Пришли ссылку на машину с сайта mobile.de!"
    )


async def url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Обрабатываю ссылку..."
    )
    # TODO: Добавить поддержку несольких ссылок
    links = [message.text[link.offset: link.offset + link.length] for link in
             filter(lambda x: x.type == MessageEntity.URL, message.entities)]
    info = MobileDe(links[0]).info()
    print(info)


if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv("TG_TOKEN")).build()

    start_handler = CommandHandler('start', start)
    url_handler = MessageHandler(~filters.COMMAND & filters.Entity(MessageEntity.URL), url)
    application.add_handler(start_handler)
    application.add_handler(url_handler)

    application.run_polling()
