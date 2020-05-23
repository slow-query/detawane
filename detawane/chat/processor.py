class Processor:
    def __init__(self, video, adapter):
        self.video = video
        self.adapter = adapter(video)
        self.filters = []
        self.handlers = []

    def __del__(self):
        del self.adapter
        self.filters.clear()
        self.handlers.clear()

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
