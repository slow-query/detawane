import time
from datetime import datetime

class Message:
    @classmethod
    def parse(cls, chat_data):
        messages = []

        chat_data_size = len(chat_data['items'])
        if chat_data_size == 0:
            return messages

        sleep_time = chat_data['pollingIntervalMillis'] / chat_data_size / 1000

        for raw_message in chat_data['items']:
            snippet = raw_message.get('snippet')
            if not snippet:
                continue
            author = raw_message['authorDetails']
            messages.append(
                cls(
                    name = author['displayName'],
                    channel_id = author['channelId'],
                    text = snippet['displayMessage'],
                    published_at = datetime.strptime(snippet['publishedAt'], '%Y-%m-%dT%H:%M:%S.%fZ'),
                    is_owner = author['isChatOwner'],
                    is_sponsor = author['isChatSponsor']
                )
            )
            time.sleep(sleep_time)

        return messages

    def __init__(self, name, channel_id, text, published_at, is_owner, is_sponsor):
        self.name = name
        self.channel_id = channel_id
        self.text = text
        self.published_at = published_at
        self.is_owner = is_owner
        self.is_sponsor = is_sponsor


