from datetime import datetime, timedelta
from .base_filter import BaseFilter

class PostPerHourFilter(BaseFilter):
    def __init__(self, video):
        super().__init__(video)
        self.store = {}

    def _is_selected(self, message):
        last_post_at = self.store.get(message.name) or datetime.fromtimestamp(0)
        if (message.published_at - last_post_at) > timedelta(hours=1):
            self.store[message.name] = message.published_at
            return True
        return False
