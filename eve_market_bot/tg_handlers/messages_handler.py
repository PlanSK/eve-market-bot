from typing import TYPE_CHECKING
from telegram import Update
from telegram.ext import ContextTypes
from loguru import logger


if TYPE_CHECKING:
    from telegram import Message, User, Chat


async def messages_main_handler(update: Update,
                                context: ContextTypes.DEFAULT_TYPE) -> None:
    """Main handler for working with user messages."""
    try:
        assert isinstance(update.message, Message)
        assert isinstance(update.effective_user, User)
        assert isinstance(update.effective_chat, Chat)
        if update.message.text:
            entered_message: str = update.message.text.upper().strip()
            if "ПРИВЕТ" in entered_message:
                logger.debug(
                    f"User({update.effective_user.id}) say keyword 'Hello'."
                )
                await update.message.reply_text(
                    f"Hello, {update.effective_user.first_name}!"
                )
            else:
                logger.debug(f"User({update.effective_user.id}) sent a message.")
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=f"I don't know what to say."
                )
    except AssertionError as exception:
        logger.error(f'Asserion error {exception} in messeges main handler.')
