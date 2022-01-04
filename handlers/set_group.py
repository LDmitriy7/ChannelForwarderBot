from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State
from aiogram.utils import exceptions

import api
import commands
import texts
from loader import dp

SET_GROUP_STATE = State('set:group')


@dp.message_handler(commands=commands.SET_GROUP, state='*')
async def ask_for_group(msg: types.Message):
    await SET_GROUP_STATE.set()
    await msg.answer(texts.show_me_group)


@dp.message_handler(state=SET_GROUP_STATE)
async def set_group(msg: types.Message, state: FSMContext):
    target_chat_id = msg.text

    try:
        target_chat = await dp.bot.get_chat(target_chat_id)
    except exceptions.TelegramAPIError:
        await msg.answer(texts.chat_not_found)
        return

    if target_chat.type not in [types.ChatType.GROUP, types.ChatType.SUPERGROUP]:
        await msg.answer(texts.show_me_group)
        return

    me = await dp.bot.me
    me_member = await target_chat.get_member(me.id)

    if not me_member or not me_member.is_chat_member():
        await msg.answer(texts.check_if_bot_chat_member)
        return

    api.set_group(target_chat.id)

    text = texts.set_group_is.format(group_id=target_chat.id, group_url=await target_chat.get_url())
    await msg.answer(text)

    await state.finish()
