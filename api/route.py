from typing import Optional

from models import documents


def get_route() -> Optional[documents.Route]:
    return documents.Route.objects.first()


def set_channel(channel_id: int):
    route = get_route() or documents.Route()
    route.channel_id = channel_id
    route.save()


def set_group(group_id: int):
    route = get_route() or documents.Route()
    route.group_id = group_id
    route.save()
