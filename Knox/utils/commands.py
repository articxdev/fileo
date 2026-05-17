from pyrogram.types import BotCommand, BotCommandScopeChat, BotCommandScopeDefault

from Knox.bot import StreamBot
from Knox.utils.logger import logger
from Knox.vars import Var

USER_COMMANDS = {
    "start": "Start the bot",
    "help": "How to use File To Link",
    "about": "About this bot",
    "ping": "Check if the bot is online",
    "dc": "Data center info for user or file",
    "link": "(Groups) Get stream & download link for a file",
}

ADMIN_COMMANDS = {
    "status": "Server status and workload",
    "stats": "System statistics",
    "users": "Total registered users",
    "broadcast": "Message all users",
    "ban": "Ban a user",
    "unban": "Unban a user",
    "authorize": "Grant permanent access",
    "deauthorize": "Revoke permanent access",
    "listauth": "List authorized users",
    "log": "Download bot logs",
    "restart": "Update and restart",
    "shell": "Run shell command",
    "speedtest": "Network speed test",
}


def _to_commands(mapping: dict) -> list:
    return [BotCommand(name, desc) for name, desc in mapping.items()]


async def set_commands():
    if not Var.SET_COMMANDS:
        return
    try:
        user_cmds = _to_commands(USER_COMMANDS)
        if user_cmds:
            await StreamBot.set_bot_commands(user_cmds, scope=BotCommandScopeDefault())
            logger.info("User commands registered (admin commands hidden from menu).")

        if Var.OWNER_ID:
            admin_cmds = _to_commands(ADMIN_COMMANDS)
            if admin_cmds:
                await StreamBot.set_bot_commands(
                    admin_cmds,
                    scope=BotCommandScopeChat(chat_id=Var.OWNER_ID),
                )
                logger.info("Admin commands registered for owner only.")
    except Exception as e:
        logger.error(f"Failed to set bot commands: {e}", exc_info=True)
