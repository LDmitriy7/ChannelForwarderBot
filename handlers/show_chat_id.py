from aiogram import types

import commands
from loader import dp


@dp.message_handler(commands=commands.SHOW_CHAT_ID, state='*')
async def show_chat_id(msg: types.Message):
    await msg.answer(f'ID этого чата: <code>{msg.chat.id}</code>')
