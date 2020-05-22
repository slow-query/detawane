import os
import tweepy
from .base_output import BaseOutput
from ..logger import get_local_logger

class Client:
    def __init__(self):
        auth = tweepy.OAuthHandler(os.environ['TWITTER_CONSUMER_KEY'], os.environ['TWITTER_CONSUMER_SECRET'])
        auth.set_access_token(os.environ['TWITTER_ACCESS_KEY'], os.environ['TWITTER_ACCESS_SECRET'])
        self.api = tweepy.API(auth)
        self._logger = get_local_logger(__name__)

    def tweet(self, text):
        self.api.update_status(text)

class TwitterOutput(BaseOutput):
    CLIENT = Client()

    def __init__(self, video):
        super().__init__(video)

    def __call__(self, message):
        self._logger.info(f'[{self.video.channel.owner_name}][{message.published_at}][{message.name}] {message.text}')
        text = f'{self.video.channel.owner_name}が「{self.video.title}」に現れました。 {self.video.url}'
        self.CLIENT.tweet(text)
