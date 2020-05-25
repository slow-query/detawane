from .adapter.pychat import Pychat
from .adapter.youtube_api import YoutubeAPI
from .filter.channel_owner_filter import ChannelOwnerFilter
from .filter.post_per_hour_filter import PostPerHourFilter
from .handler.stdout_handler import StdoutHandler
from .handler.twitter_handler import TwitterHandler
from .processor import Processor

ADAPTER_TYPES = {"pychat": Pychat, "api": YoutubeAPI}


def build_processor(type, video):
    processor = Processor(video, ADAPTER_TYPES[type])
    processor.add_filter(ChannelOwnerFilter)
    processor.add_filter(PostPerHourFilter)
    processor.add_handler(StdoutHandler)
    processor.add_handler(TwitterHandler)

    return processor
