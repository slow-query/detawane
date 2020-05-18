#!/usr/bin/env python3
from .message import Message
from .filter.channel_owner_filter import ChannelOwnerFilter
from .filter.post_per_hour_filter import PostPerHourFilter
from .output.stdout_output import StdoutOutput

class MessageProcessor:
    DEFAULT_FILTER_CLASSES = [ChannelOwnerFilter, PostPerHourFilter]
    DEFAULT_OUTPUT_CLASS = StdoutOutput

    def __init__(self, video, filter_classes = DEFAULT_FILTER_CLASSES, output_class = DEFAULT_OUTPUT_CLASS):
        self.video = video
        self.filters = [filter_class(video) for filter_class in filter_classes]
        self.output = output_class(video)

    def __call__(self, chat_data):
        messages = self._filtered_messages(
            Message.parse(chat_data)
        )
        for message in messages:
            self.output(message)

    def _filtered_messages(self, messages):
        for filter in self.filters:
            messages = filter(messages)
        return messages
