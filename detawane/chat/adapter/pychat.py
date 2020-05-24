from datetime import datetime

from pytchat import CompatibleProcessor, LiveChat

from ..message import Message


class Pychat:
    def __init__(self, video):
        self.live_chat = LiveChat(video_id=video.id, processor=CompatibleProcessor())

    def __del__(self):
        self.live_chat.terminate()

    def get_messages(self):
        return self._parse(self.live_chat.get())

    def _parse(self, chat_data):
        messages = []
        chat_data_size = len(chat_data["items"])
        if chat_data_size == 0:
            return messages

        for raw_message in chat_data["items"]:
            snippet = raw_message.get("snippet")
            if not snippet:
                continue
            author = raw_message["authorDetails"]
            messages.append(
                Message(
                    name=author["displayName"],
                    channel_id=author["channelId"],
                    text=snippet["displayMessage"],
                    published_at=datetime.strptime(
                        snippet["publishedAt"], "%Y-%m-%dT%H:%M:%S.%fZ"
                    ),
                    is_owner=author["isChatOwner"],
                    is_sponsor=author["isChatSponsor"],
                )
            )

        return messages
