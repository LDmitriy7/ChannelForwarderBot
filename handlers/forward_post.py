from aiogram import types

from loader import dp
from models import documents


@dp.channel_post_handler()
async def forward_post(msg: types.Message):
    route: documents.Route = documents.Route.objects.first()

    if not route:
        return

    if route.group_id and route.channel_id == msg.chat.id:
        await msg.forward(route.group_id)
