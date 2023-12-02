from telegram.ext import ApplicationBuilder

from eve_market_bot.tg_lib.handlers import (
    BOT_COMMAND_HANDLERS_LIST,
    MESSAGES_MAIN_HANDLER,
    UNKNOWN_COMMAND_HANDLER
)
from eve_market_bot.settings import *


def main():
    bot_instance = ApplicationBuilder().token(TOKEN).build()
    bot_instance.add_handlers(BOT_COMMAND_HANDLERS_LIST)
    bot_instance.add_handler(MESSAGES_MAIN_HANDLER)
    bot_instance.add_handler(UNKNOWN_COMMAND_HANDLER)
    bot_instance.run_polling()


if __name__ == '__main__':
    main()
