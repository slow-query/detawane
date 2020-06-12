from pytz import timezone, utc


class Message:
    def __init__(self, name, channel_id, text, published_at, is_owner, is_sponsor):
        self.name = name
        self.channel_id = channel_id
        self.text = text
        self.published_at = published_at
        self.is_owner = is_owner
        self.is_sponsor = is_sponsor

    def published_at_jst(self):
        jst = timezone("Asia/Tokyo")
        return self.published_at.replace(tzinfo=utc).astimezone(jst)
