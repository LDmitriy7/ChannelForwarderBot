from aiogram import types
from aiogram.dispatcher import FSMContext

import commands
import texts
from loader import dp
from models import documents


@dp.message_handler(commands=commands.INFO, state='*')
async def info(msg: types.Message, state: FSMContext):
    await state.finish()

    route: documents.Route = documents.Route.objects.first()

    if not route:
        await msg.answer(texts.channel_and_group_not_set)
        return

    text = texts.channel_and_group_is(channel_id=route.channel_id, group_id=route.group_id)
    await msg.answer(text)
