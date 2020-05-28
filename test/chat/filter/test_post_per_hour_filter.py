from datetime import datetime
from unittest import TestCase
from unittest.mock import Mock

from detawane.chat.filter.post_per_hour_filter import PostPerHourFilter


class PostPerHourFilterTestCase(TestCase):
    def build_message(self, channel_id, published_at):
        message = Mock()
        message.channel_id = channel_id
        message.published_at = datetime.strptime(published_at, "%Y-%m-%d %H:%M:%S")
        return message

    def test_call(self):
        video = Mock()
        filter = PostPerHourFilter(video)
        ok_messages = [
            self.build_message("A", "2020-05-28 17:00:00"),
            self.build_message("B", "2020-05-28 17:30:00"),
            self.build_message("A", "2020-05-28 18:00:01"),
        ]
        ng_messages = [self.build_message("A", "2020-05-28 18:00:00")]

        messages = filter(
            sorted(ok_messages + ng_messages, key=lambda x: x.published_at)
        )
        self.assertEqual(messages, ok_messages)
