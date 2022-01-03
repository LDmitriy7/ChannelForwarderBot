from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State

import commands
import texts
from loader import dp

SET_CHANNEL_STATE = State('set:channel')


@dp.message_handler(commands=commands.SET_CHANNEL, state='*')
async def ask_for_channel(msg: types.Message):
    await SET_CHANNEL_STATE.set()
    await msg.answer(texts.show_me_channel)


@dp.message_handler(state=SET_CHANNEL_STATE)
async def send_keyboard(msg: types.Message, state: FSMContext):
    # try:
    #     channel = int(msg.text)
    #     await msg.answer(f'Новый ID канала: {channel}')
    # except ValueError:
    #     channel = '@' + msg.text.strip('@')
    #     await msg.answer(f'Новый юзернейм канала: {channel}')
    #
    # with shelve.open(SHELVE_FILE) as sh:
    #     sh[CHANNEL_KEY] = channel
    #
    await state.finish()
