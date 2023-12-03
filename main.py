from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, filters
)

from eve_market_bot import tg_handlers
from eve_market_bot.settings import *


BOT_COMMAND_HANDLERS = {
    "start": tg_handlers.start,
}


def main():
    bot_application = ApplicationBuilder().token(TOKEN).build()

    for command, handler in BOT_COMMAND_HANDLERS.items():
        bot_application.add_handler(CommandHandler(command, handler))

    bot_application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND, tg_handlers.messages_handler
        )
    )
    bot_application.add_handler(
        MessageHandler(filters.COMMAND, tg_handlers.unknown)
    )

    bot_application.run_polling()


if __name__ == '__main__':
    main()
