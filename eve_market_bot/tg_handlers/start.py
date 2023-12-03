from telegram import Update
from telegram.ext import ContextTypes
from loguru import logger

from eve_market_bot.db import db_instance

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a welcome message for the user"""
    logger.debug(
        f'User({update.effective_user.id}) has started working with the bot.'
    )
    first_name = update.effective_chat.first_name
    result = db_instance.add_user(
        id=update.effective_user.id,
        first_name=first_name,
        last_name=update.effective_user.last_name
    )
    greeting = f"Hello, {first_name}! I'm new EVE Online Market Bot."
    if not result:
        greeting = f"Welcome again, {first_name}"

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=greeting
    )
