from .filter.channel_owner_filter import ChannelOwnerFilter
from .filter.post_per_hour_filter import PostPerHourFilter
from .handler.stdout_handler import StdoutHandler
from .handler.twitter_handler import TwitterHandler
from .processor import Processor


def build_processor(video, adapter):
    processor = Processor(video, adapter)
    processor.add_filter(ChannelOwnerFilter)
    processor.add_filter(PostPerHourFilter)
    processor.add_handler(StdoutHandler)
    processor.add_handler(TwitterHandler)

    return processor
