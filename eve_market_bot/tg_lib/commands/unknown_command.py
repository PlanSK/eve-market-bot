from telegram import Update
from telegram.ext import ContextTypes
from loguru import logger


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Function for processing unknown commands.
    Sends a message that the command is unknown to the bot.
    """
    logger.debug(
        f'User({update.effective_user.id}) has entered an unknown '
        f'command "{update.message.text}".'
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Sorry, I didn't understand that command."
    )
