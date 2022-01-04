from contextlib import suppress

from aiogram import types
from aiogram.utils.exceptions import TelegramAPIError

import config
from loader import dp

START = 'start'
CANCEL = 'cancel'
INFO = 'info'
SET_CHANNEL = 'set_channel'
SET_GROUP = 'set_group'
SHOW_CHAT_ID = 'show_chat_id'

USER_COMMANDS = [
    types.BotCommand(SHOW_CHAT_ID, 'Показать ID этого чата'),
]

ADMIN_COMMANDS = USER_COMMANDS + [
    types.BotCommand(INFO, 'Посмотреть канал и группу'),
    types.BotCommand(SET_CHANNEL, 'Задать канал'),
    types.BotCommand(SET_GROUP, 'Задать группу'),
]


async def setup():
    await dp.bot.set_my_commands(USER_COMMANDS)

    for user_id in config.Users.admins_ids:
        with suppress(TelegramAPIError):
            await dp.bot.set_my_commands(ADMIN_COMMANDS, scope=types.BotCommandScopeChat(user_id))
