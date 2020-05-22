class BaseFilter:
    def __init__(self, video):
        self.video = video

    def __call__(self, messages):
        return [message for message in messages if self._is_selected(message)]

    def _is_selected(self, message):
        pass
