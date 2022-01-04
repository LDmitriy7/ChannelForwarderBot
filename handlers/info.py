from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils import exceptions

import api
import commands
import texts
from loader import dp


@dp.message_handler(commands=commands.INFO, state='*')
async def info(msg: types.Message, state: FSMContext):
    await state.finish()

    route = api.get_route()

    if not route:
        await msg.answer(texts.channel_and_group_not_set)
        return

    try:
        channel = await dp.bot.get_chat(route.channel_id)
    except exceptions.TelegramAPIError:
        channel_url = None
    else:
        channel_url = await channel.get_url()

    try:
        group = await dp.bot.get_chat(route.group_id)
    except exceptions.TelegramAPIError:
        group_url = None
    else:
        group_url = await group.get_url()

    channel_text = texts.set_channel_is.format(channel_id=route.channel_id, channel_url=channel_url)
    group_text = texts.set_group_is.format(group_id=route.group_id, group_url=group_url)

    await msg.answer(channel_text)
    await msg.answer(group_text)
