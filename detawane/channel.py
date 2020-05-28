class Channel:
    def __init__(self, id, owner_name):
        self.id = id
        self.owner_name = owner_name
        self.url = "https://www.youtube.com/channel/" + id
