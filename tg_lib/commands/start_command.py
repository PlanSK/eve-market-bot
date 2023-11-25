from telegram import Update
from telegram.ext import ContextTypes
from loguru import logger


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a welcome message for the user"""
    logger.debug(
        f'User({update.effective_user.id}) has started working with the bot.'
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello! I'm new EVE Online Market Bot."
    )
