import json
from datetime import datetime
from unittest import TestCase

from detawane.chat.adapter.parser.youtube_parser import YoutubeParser


class YoutubeParserTestCase(TestCase):
    DATA = """
{
  "kind": "youtube#liveChatMessageListResponse",
  "etag": "cWwGy2-CsGLUVm0A0sOeIKlDh38",
  "pollingIntervalMillis": 5091,
  "pageInfo": {
    "totalResults": 73,
    "resultsPerPage": 73
  },
  "nextPageToken": "GMvtla-jzukCIJblx7OjzukC",
  "items": [
    {
      "kind": "youtube#liveChatMessage",
      "etag": "t7UDaoStg44_NqF56lhsy-qStAw",
      "id": "発言のID",
      "snippet": {
        "type": "textMessageEvent",
        "liveChatId": "ライブチャットのID",
        "authorChannelId": "A",
        "publishedAt": "2020-05-25T05:23:43.374000Z",
        "hasDisplayContent": true,
        "displayMessage": "Aの発言",
        "textMessageDetails": {
          "messageText": "Aの発言"
        }
      },
      "authorDetails": {
        "channelId": "A",
        "channelUrl": "http://www.youtube.com/channel/A",
        "displayName": "Aさん",
        "profileImageUrl": "photo.jpg",
        "isVerified": false,
        "isChatOwner": false,
        "isChatSponsor": true,
        "isChatModerator": false
      }
    }
  ]
}
"""

    def setUp(self):
        self.parser = YoutubeParser()

    def test_call(self):
        chat_data = json.loads(self.DATA)
        messages = self.parser(chat_data)
        self.assertEqual(len(messages), 1)

        source = chat_data["items"][0]
        self.assertEqual(messages[0].name, source["authorDetails"]["displayName"])
        self.assertEqual(messages[0].channel_id, source["authorDetails"]["channelId"])
        self.assertEqual(messages[0].text, source["snippet"]["displayMessage"])
        self.assertEqual(
            messages[0].published_at,
            datetime.strptime(
                source["snippet"]["publishedAt"], "%Y-%m-%dT%H:%M:%S.%fZ"
            ),
        )
        self.assertEqual(messages[0].is_owner, False)
        self.assertEqual(messages[0].is_sponsor, True)
