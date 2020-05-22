from .base_filter import BaseFilter

class ChannelOwnerFilter(BaseFilter):
    def _is_selected(self, message):
        return self.video.channel.id == message.channel_id
