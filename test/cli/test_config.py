from unittest import TestCase
from unittest.mock import mock_open, patch

from detawane.channel import Channel
from detawane.chat.adapter.pychat import Pychat
from detawane.chat.adapter.youtube_api import YoutubeAPI
from detawane.cli.config import Config
from detawane.video import Video


class ConfigTestCase(TestCase):
    DATA = """
[
  {
    "id": "チャンネルのID",
    "name": "チャンネル主の名前",
    "videos": [
      {
        "id": "ビデオのID",
        "title": "ビデオのタイトル",
        "start_at": "2021-02-27 14:00:00+00:00",
        "chat_id": "チャットのID",
        "channel": {
          "id": "チャンネルのID（削除予定）",
          "title": "チャンネルのタイトル（削除予定）"
        }
      }
    ]
  }
]
"""

    @patch("builtins.open", mock_open(read_data=DATA))
    def test_adapter(self):
        patterns = [
            (Pychat, ["-", "--file", "test.json"]),
            (YoutubeAPI, ["-", "--file", "test.json", "--adapter", "api"]),
            (Pychat, ["-", "--file", "test.json", "--adapter", "pychat"]),
        ]

        for expected_class, argv in patterns:
            with self.subTest(expected_class=expected_class, argv=argv):
                with patch("sys.argv", argv):
                    config = Config()
                    self.assertEqual(config.adapter, expected_class)

    @patch("builtins.open", mock_open(read_data=DATA))
    def test_videos(self):
        with patch("sys.argv", ["-", "--file", "test.json"]):
            config = Config()
            self.assertEqual(len(config.videos), 1)
            video = config.videos[0]
            self.assertIsInstance(video, Video)
            self.assertEqual(video.id, "ビデオのID")
            channel = video.channel
            self.assertIsInstance(channel, Channel)
            self.assertEqual(channel.id, "チャンネルのID")
