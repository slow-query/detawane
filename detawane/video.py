class Video:
    def __init__(self, channel, id, title, chat_id):
        self.channel = channel
        self.id = id
        self.title = title
        self.chat_id = chat_id
        self.url = "https://www.youtube.com/watch?v=" + id
