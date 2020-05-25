import signal
import time


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
            time_mark = time.time()
            for processor in processors:
                processor.process()
            remaining_time = self.MAX_PROCESSING_TIME - (time.time() - time_mark)
            time.sleep(remaining_time if remaining_time > 0 else 0)

        for processor in processors:
            processor.finalize()
