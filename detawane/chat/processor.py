from datetime import datetime

from ..logger import get_local_logger


class Processor:
    def __init__(self, video, adapter, logger=get_local_logger(__name__)):
        self.video = video
        self.adapter = adapter(video)
        self.filters = []
        self.handlers = []
        self._logger = logger

    def initialize(self):
        self._logger.info(
            f"{self.video.channel.owner_name}の「{self.video.title}」の監視を開始しました。"
        )

    def finalize(self):
        self.adapter.terminate()
        self.filters.clear()
        self.handlers.clear()
        self._logger.info(
            f"{self.video.channel.owner_name}の「{self.video.title}」の監視を終了しました。"
        )

    def add_filter(self, filter_class):
        self.filters.append(filter_class(self.video))

    def add_handler(self, handler_class):
        self.handlers.append(handler_class(self.video))

    def process(self):
        messages = self.adapter.get_messages()
        for filter in self.filters:
            messages = filter(messages)

        for handler in self.handlers:
            for message in messages:
                handler(message)

    def is_expired(self, time=datetime.now()):
        return self.video.start_at.timestamp() < time.timestamp()
