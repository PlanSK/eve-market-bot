from telegram.ext import CommandHandler, MessageHandler, filters

from tg_lib.messages_handler import messages_main_handler
from tg_lib.commands.start_command import start
from tg_lib.commands.unknown_command import unknown
from tg_lib.commands.hello_world_command import hello_world


MESSAGES_MAIN_HANDLER = MessageHandler(filters.TEXT & ~filters.COMMAND,
                                       messages_main_handler)
UNKNOWN_COMMAND_HANDLER = MessageHandler(filters.COMMAND, unknown)
BOT_COMMAND_HANDLERS_LIST = [
    CommandHandler('start', start),
    CommandHandler('hello_world', hello_world),
]
