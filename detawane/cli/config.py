from argparse import ArgumentParser

from ..chat.adapter.pychat import Pychat
from ..chat.adapter.youtube_api import YoutubeAPI
from .video_list import VideoList


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
        return VideoList.load(file)

    def _fetch_adapter(self, adapter_type):
        return self.ADAPTER_TABLES[adapter_type]
