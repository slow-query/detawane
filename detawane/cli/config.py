import json
from argparse import ArgumentParser
from datetime import datetime

from ..channel import Channel
from ..chat.adapter.pychat import Pychat
from ..chat.adapter.youtube_api import YoutubeAPI
from ..video import Video


class Config:
    ADAPTER_TABLES = {"pychat": Pychat, "api": YoutubeAPI}

    def __init__(self):
        args = self._parse_args()

        self.videos = self._load_videos(args.file)
        self.adapter = self._fetch_adapter(args.adapter)

    def _parse_args(self):
        parser = ArgumentParser()
        parser.add_argument(
            "--file", "-f", type=str, required=True, help="specify channel list file"
        )
        parser.add_argument(
            "--adapter",
            "-a",
            type=str,
            default="pychat",
            metavar="ADAPTER_TYPE",
            help="select either pychat or api",
        )
        return parser.parse_args()

    def _load_videos(self, file):
        videos = []
        for channel in json.load(open(file, "r")):
            for video in channel["videos"]:
                videos.append(
                    Video(
                        channel=Channel(id=channel["id"], owner_name=channel["name"]),
                        id=video["id"],
                        title=video["title"],
                        chat_id=video["chat_id"],
                        start_at=datetime.strptime(
                            video["start_at"], "%Y-%m-%d %H:%M:%S%z"
                        ),
                    )
                )
        return videos

    def _fetch_adapter(self, adapter_type):
        return self.ADAPTER_TABLES[adapter_type]
