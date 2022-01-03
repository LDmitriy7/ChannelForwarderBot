import mongoengine as me


class Route(me.Document):
    channel_id: int = me.IntField()
    group_id: int = me.IntField()
