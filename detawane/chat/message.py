class Message:
    def __init__(self, name, channel_id, text, published_at, is_owner, is_sponsor):
        self.name = name
        self.channel_id = channel_id
        self.text = text
        self.published_at = published_at
        self.is_owner = is_owner
        self.is_sponsor = is_sponsor
