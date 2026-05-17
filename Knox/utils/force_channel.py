# Knox/utils/force_channel.py

import asyncio

from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, Message

from Knox.utils.keyboard import join_channel_markup

from Knox.utils.logger import logger
from Knox.utils.messages import MSG_COMMUNITY_CHANNEL
from Knox.vars import Var

_force_link = None
_force_title = None

async def get_force_info(bot: Client):
    global _force_link, _force_title
    
    if not Var.FORCE_CHANNEL_ID:
        return None, None
    
    if _force_link is not None and _force_title is not None:
        return _force_link, _force_title
    
    try:
        try:
            chat = await bot.get_chat(Var.FORCE_CHANNEL_ID)
        except FloodWait as e:
            await asyncio.sleep(e.value)
            chat = await bot.get_chat(Var.FORCE_CHANNEL_ID)
        if chat:
            _force_link = chat.invite_link or (f"https://t.me/{chat.username}" if chat.username else None)
            _force_title = chat.title or "Channel"
        return _force_link, _force_title
    except Exception as e:
        logger.error(f"Force channel error: {e}", exc_info=True)
        return None, None

async def force_channel_check(client: Client, message: Message):
    if not Var.FORCE_CHANNEL_ID:
        return True
    
    if message.from_user is None:
        return True

    try:
        while True:
            try:
                member = await client.get_chat_member(Var.FORCE_CHANNEL_ID, message.from_user.id)
                if member is None:
                    logger.error(f"Failed to get chat member for {message.from_user.id} in force channel {Var.FORCE_CHANNEL_ID} after retries.")
                    return False
                return True
            except FloodWait as e:
                logger.debug(f"FloodWait in force_channel_check, sleeping for {e.value}s")
                await asyncio.sleep(e.value)
    except UserNotParticipant:
        link, title = await get_force_info(client)
        join_row = join_channel_markup(title or "Channel", link)
        kb = InlineKeyboardMarkup([join_row]) if join_row else None
        try:
            await message.reply_text(
                MSG_COMMUNITY_CHANNEL.format(channel_title=title or "Channel"),
                reply_markup=kb,
            )
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await message.reply_text(
                MSG_COMMUNITY_CHANNEL.format(channel_title=title or "Channel"),
                reply_markup=kb,
            )
        else:
            try:
                await message.reply_text("You must join the channel to use this bot.")
            except FloodWait as e:
                await asyncio.sleep(e.value)
                await message.reply_text("You must join the channel to use this bot.")
        return False
    except Exception as e:
        logger.error(f"Error checking force channel: {e}", exc_info=True)
        try:
            await message.reply_text("An unexpected error occurred while checking channel membership. Please try again.")
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await message.reply_text("An unexpected error occurred while checking channel membership. Please try again.")
        return False
