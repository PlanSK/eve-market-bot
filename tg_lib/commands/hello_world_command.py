from telegram import Update
from telegram.ext import ContextTypes
from loguru import logger


async def hello_world(update: Update,
                      context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends 'Hello world.' for the user"""
    logger.debug(
        f'User({update.effective_user.id}) has called "hello_world" command.'
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Hello world, {update.effective_user.first_name}"
    )
