from datetime import datetime

from ...message import Message


class YoutubeParser:
    def __call__(self, chat_data):
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
