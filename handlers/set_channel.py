from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State
from aiogram.utils import exceptions

import api
import commands
import texts
from loader import dp

SET_CHANNEL_STATE = State('set:channel')


@dp.message_handler(commands=commands.SET_CHANNEL, state='*')
async def ask_for_channel(msg: types.Message):
    await SET_CHANNEL_STATE.set()
    await msg.answer(texts.show_me_channel)


@dp.message_handler(state=SET_CHANNEL_STATE, content_types='any')
async def set_channel(msg: types.Message, state: FSMContext):
    if msg.forward_from_chat:
        target_chat_id = msg.forward_from_chat.id
    elif msg.text:
        target_chat_id = msg.text
    else:
        await msg.answer(texts.show_me_channel)
        return

    try:
        target_chat = await dp.bot.get_chat(target_chat_id)
    except exceptions.TelegramAPIError:
        await msg.answer(texts.chat_not_found)
        return

    if target_chat.type != types.ChatType.CHANNEL:
        await msg.answer(texts.show_me_channel)
        return

    me = await dp.bot.me
    me_member = await target_chat.get_member(me.id)

    if not me_member or not me_member.is_chat_member():
        await msg.answer(texts.check_if_bot_chat_member)
        return

    api.set_channel(target_chat.id)

    text = texts.set_channel_is.format(channel_id=target_chat.id, channel_url=await target_chat.get_url())
    await msg.answer(text)

    await state.finish()
