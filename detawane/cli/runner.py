import signal

from ..time_keeper import keep_time


class Runner:
    MAX_PROCESSING_TIME = 5

    def __init__(self):
        self._is_running = True

        signal.signal(signal.SIGINT, self._terminate)
        signal.signal(signal.SIGTERM, self._terminate)

    def _terminate(self, num, frame):
        self._is_running = False

    def run(self, processors):
        for processor in processors:
            processor.initialize()

        while self._is_running:
            with keep_time(self.MAX_PROCESSING_TIME):
                for processor in processors:
                    processor.process()
                for processor in [p for p in processors if p.is_expired()]:
                    processors.remove(processor)
                    processor.finalize()

        for processor in processors:
            processor.finalize()
