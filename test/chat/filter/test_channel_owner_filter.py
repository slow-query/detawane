from unittest import TestCase
from unittest.mock import Mock

from detawane.chat.filter.channel_owner_filter import ChannelOwnerFilter


class ChannelOwnerFilterTestCase(TestCase):
    def build_message(self, channel_id):
        message = Mock()
        message.channel_id = channel_id
        return message

    def test_call(self):
        video = Mock()
        video.channel.id = "OwnerID"
        filter = ChannelOwnerFilter(video)
        owner_message = self.build_message("OwnerID")
        non_owner_message = self.build_message("NonOwnerID")

        messages = filter([owner_message, non_owner_message])
        self.assertEqual(messages, [owner_message])
