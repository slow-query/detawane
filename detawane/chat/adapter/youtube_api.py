import os
import queue
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

from googleapiclient.discovery import build

from ..message import Message


class YoutubeAPI:
    def __init__(self, video):
        self._is_active = True
        self.video = video
        self._client = build(
            "youtube", "v3", developerKey=os.environ["YOUTUBE_API_KEY"]
        )
        self._buffer = queue.Queue(maxsize=20)
        self._executor = ThreadPoolExecutor(max_workers=1)

        self._executor.submit(self._listen)

    def terminate(self):
        self._is_active = False

    def get_messages(self):
        return [] if self._buffer.empty() else self._parse(self._buffer.get())

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

    def _listen(self):
        next_page_token = None

        while self._is_active:
            time_mark = time.time()
            res = (
                self._client.liveChatMessages()
                .list(
                    liveChatId=self.video.chat_id,
                    part="snippet,authorDetails",
                    pageToken=next_page_token,
                )
                .execute()
            )

            cool_time_ms = res["pollingIntervalMillis"] or 10_000
            cool_time = cool_time_ms / 1_000
            next_page_token = res["nextPageToken"]

            self._buffer.put(res)

            remaining_time = cool_time - (time.time() - time_mark)
            time.sleep(remaining_time if remaining_time > 0 else 0)
