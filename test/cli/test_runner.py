from threading import Timer
from unittest import TestCase
from unittest.mock import Mock

from detawane.cli.runner import Runner


class RunnnerTestCase(TestCase):
    def setUp(self):
        self.runner = Runner()
        self.runner.MAX_PROCESSING_TIME = 0

    def stop_running(self):
        self.runner._is_running = False

    def test_run_calls_each_method(self):
        timer = Timer(1, self.stop_running)
        timer.start()

        test_process = Mock()
        self.runner.run([test_process])

        test_process.initialize.assert_called_once()
        test_process.process.assert_called()
        test_process.finalize.assert_called_once()
