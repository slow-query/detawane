import json


class Channel:
    def __init__(self, id, owner_name):
        self.id = id
        self.owner_name = owner_name
        self.url = "https://www.youtube.com/channel/" + id


class Video:
    def __init__(self, channel, id, title):
        self.channel = channel
        self.id = id
        self.title = title
        self.url = "https://www.youtube.com/watch?v=" + id


class VideoList:
    def load(file_path):
        videos = []
        for channel in json.load(open(file_path, "r")):
            for video in channel["videos"]:
                videos.append(
                    Video(
                        channel=Channel(id=channel["id"], owner_name=channel["name"]),
                        id=video["id"],
                        title=video["title"],
                    )
                )
        return videos
