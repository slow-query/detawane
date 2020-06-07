import time
from datetime import datetime
from unittest import TestCase, skip
from unittest.mock import Mock

from detawane.chat.processor import Processor


class ProcessorTestCase(TestCase):
    def to_time(self, str):
        return time.mktime(time.strptime(str, "%Y-%m-%d %H:%M:%S"))

    def setUp(self):
        video = Mock()
        adapter_class = Mock()
        logger = Mock()

        self.adapter = adapter_class.return_value
        self.video = video
        self.logger = logger
        self.processor = Processor(video, adapter_class, logger)

    @skip("Pending")
    def test_initialize(self):
        pass

    def test_finalize(self):
        self.processor.add_filter(Mock())
        self.processor.add_handler(Mock())
        self.assertNotEqual(len(self.processor.filters), 0)
        self.assertNotEqual(len(self.processor.handlers), 0)

        self.processor.finalize()
        self.assertEqual(len(self.processor.filters), 0)
        self.assertEqual(len(self.processor.handlers), 0)
        self.adapter.terminate.assert_called_once()

    def test_add_filter(self):
        filter_class = Mock()
        filter_class_instance = filter_class.return_value

        self.processor.add_filter(filter_class)
        self.assertEqual(self.processor.filters, [filter_class_instance])

    def test_add_handler(self):
        handler_class = Mock()
        handler_class_instance = handler_class.return_value

        self.processor.add_handler(handler_class)
        self.assertEqual(self.processor.handlers, [handler_class_instance])

    def test_process(self):
        # filter
        messages = [Mock()]
        filter_class = Mock()
        filter_class_instance = filter_class.return_value
        self.processor.add_filter(filter_class)
        self.adapter.get_messages.return_value = messages

        # handler
        filtered_message = Mock()
        filter_class_instance.return_value = [filtered_message]
        handler_class = Mock()
        handler_class_instance = handler_class.return_value
        self.processor.add_handler(handler_class)

        self.processor.process()
        filter_class_instance.assert_called_once_with(messages)
        handler_class_instance.assert_called_once_with(filtered_message)

    def test_is_expired(self):
        self.processor.video.start_at = datetime.strptime(
            "2020-06-07 10:00:00", "%Y-%m-%d %H:%M:%S"
        )
        self.assertTrue(self.processor.is_expired(self.to_time("2020-06-07 10:00:01")))
        self.assertFalse(self.processor.is_expired(self.to_time("2020-06-07 9:59:59")))
