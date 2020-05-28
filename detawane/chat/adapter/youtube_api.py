import os
import queue
import time
from concurrent.futures import ThreadPoolExecutor

from googleapiclient.discovery import build

from .parser.youtube_parser import YoutubeParser


class YoutubeAPI:
    def __init__(self, video, parser=YoutubeParser):
        self._is_active = True
        self.video = video
        self._parser = parser
        self._client = build(
            "youtube", "v3", developerKey=os.environ["YOUTUBE_API_KEY"]
        )
        self._buffer = queue.Queue(maxsize=20)
        self._executor = ThreadPoolExecutor(max_workers=1)

        self._executor.submit(self._listen)

    def terminate(self):
        self._is_active = False

    def get_messages(self):
        return [] if self._buffer.empty() else self._parser(self._buffer.get())

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
