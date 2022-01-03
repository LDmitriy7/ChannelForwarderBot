from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

import config


class CheckAccess(BaseMiddleware):

    @staticmethod
    async def on_pre_process_message(msg: types.Message, *_):
        if msg.from_user.id not in config.Users.admins_ids:
            raise CancelHandler

    @staticmethod
    async def on_pre_process_callback_query(query: types.CallbackQuery, *_):
        if query.from_user.id not in config.Users.admins_ids:
            raise CancelHandler
