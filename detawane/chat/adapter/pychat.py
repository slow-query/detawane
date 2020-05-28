from pytchat import CompatibleProcessor, LiveChat

from .parser.youtube_parser import YoutubeParser


class Pychat:
    def __init__(self, video, parser=YoutubeParser()):
        self.live_chat = LiveChat(video_id=video.id, processor=CompatibleProcessor())
        self._parser = parser

    def terminate(self):
        self.live_chat.terminate()

    def get_messages(self):
        return self._parser(self.live_chat.get())
