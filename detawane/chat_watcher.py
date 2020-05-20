#!/usr/bin/env python3

from pytchat import LiveChat, CompatibleProcessor
from .message_processor import MessageProcessor

class ChatWatcher:
    def __init__(self, video, output_class):
        self.video = video
        message_processor = MessageProcessor(
            video = video,
            output_class = output_class
        )
        self.live_chat = LiveChat(video_id = video.id, callback = message_processor, processor = CompatibleProcessor())

    def __del__(self):
        self.live_chat.terminate()
