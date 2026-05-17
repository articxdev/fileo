# Knox/utils/keyboard.py

from typing import List, Optional
from urllib.parse import urlparse

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Knox.utils.messages import (
    MSG_BUTTON_ABOUT,
    MSG_BUTTON_CLOSE,
    MSG_BUTTON_DOWNLOAD,
    MSG_BUTTON_GET_HELP,
    MSG_BUTTON_JOIN_CHANNEL,
    MSG_BUTTON_START_CHAT,
    MSG_BUTTON_STREAM_NOW,
)


def is_valid_button_url(url: Optional[str]) -> bool:
    if not url or not isinstance(url, str):
        return False
    url = url.strip()
    if len(url) > 2048:
        return False
    if url.startswith("tg://"):
        return bool(urlparse(url).path or urlparse(url).netloc)
    if not url.startswith(("http://", "https://")):
        return False
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    if not host:
        return False
    if host in ("0.0.0.0", "127.0.0.1", "localhost"):
        return False
    return True


def sanitize_button_url(url: Optional[str]) -> Optional[str]:
    return url.strip() if is_valid_button_url(url) else None


def link_markup(stream_link: str, download_link: str) -> Optional[InlineKeyboardMarkup]:
    row: List[InlineKeyboardButton] = []
    stream = sanitize_button_url(stream_link)
    download = sanitize_button_url(download_link)
    if stream:
        row.append(InlineKeyboardButton(MSG_BUTTON_STREAM_NOW, url=stream))
    if download:
        row.append(InlineKeyboardButton(MSG_BUTTON_DOWNLOAD, url=download))
    if not row:
        return None
    return InlineKeyboardMarkup([row])


def start_chat_markup(bot_username: Optional[str]) -> Optional[InlineKeyboardMarkup]:
    if not bot_username:
        return None
    url = sanitize_button_url(f"https://t.me/{bot_username}?start=start")
    if not url:
        return None
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(MSG_BUTTON_START_CHAT, url=url)]
    ])


def join_channel_markup(title: str, link: Optional[str]) -> Optional[List[InlineKeyboardButton]]:
    url = sanitize_button_url(link)
    if not url:
        return None
    return [InlineKeyboardButton(MSG_BUTTON_JOIN_CHANNEL.format(channel_title=title), url=url)]


def main_menu_markup(join_link: Optional[str] = None, join_title: str = "Channel") -> InlineKeyboardMarkup:
    rows = [
        [
            InlineKeyboardButton(MSG_BUTTON_GET_HELP, callback_data="help_command"),
            InlineKeyboardButton(MSG_BUTTON_ABOUT, callback_data="about_command"),
        ],
        [InlineKeyboardButton(MSG_BUTTON_CLOSE, callback_data="close_panel")],
    ]
    join_row = join_channel_markup(join_title, join_link)
    if join_row:
        rows.insert(1, join_row)
    return InlineKeyboardMarkup(rows)


def help_markup(join_link: Optional[str] = None, join_title: str = "Channel") -> InlineKeyboardMarkup:
    rows = [[InlineKeyboardButton(MSG_BUTTON_ABOUT, callback_data="about_command")]]
    join_row = join_channel_markup(join_title, join_link)
    if join_row:
        rows.append(join_row)
    rows.append([InlineKeyboardButton(MSG_BUTTON_CLOSE, callback_data="close_panel")])
    return InlineKeyboardMarkup(rows)


def about_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(MSG_BUTTON_GET_HELP, callback_data="help_command")],
        [InlineKeyboardButton(MSG_BUTTON_CLOSE, callback_data="close_panel")],
    ])


def token_markup(url: str) -> Optional[InlineKeyboardMarkup]:
    safe = sanitize_button_url(url)
    if not safe:
        return None
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔑 Activate Access", url=safe)]
    ])
