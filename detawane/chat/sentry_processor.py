from ..logger import get_local_logger


class SentryProcessor:
    def __init__(self, logger=get_local_logger(__name__)):
        self._logger = logger

    def initialize(self):
        self._logger.info("番兵プロセス開始")

    def finalize(self):
        self._logger.info("番兵プロセス終了")

    def add_filter(self, filter_class):
        pass

    def add_handler(self, handler_class):
        pass

    def process(self):
        pass

    def is_expired(self, time):
        return False
