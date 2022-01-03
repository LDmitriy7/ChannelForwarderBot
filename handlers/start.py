from aiogram import types
from aiogram.dispatcher import FSMContext

import commands
import texts
from loader import dp


@dp.message_handler(commands=commands.START, state='*')
async def welcome(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer(texts.welcome)
