import os

import tweepy

from ...logger import get_local_logger
from .base_handler import BaseHandler


class Client:
    def __init__(self, logger=get_local_logger(__name__)):
        auth = tweepy.OAuthHandler(
            os.environ["TWITTER_CONSUMER_KEY"], os.environ["TWITTER_CONSUMER_SECRET"]
        )
        auth.set_access_token(
            os.environ["TWITTER_ACCESS_KEY"], os.environ["TWITTER_ACCESS_SECRET"]
        )
        self.api = tweepy.API(auth)
        self._logger = logger

    def tweet(self, text):
        try:
            self.api.update_status(text)
        except tweepy.error.TweepError as e:
            self._logger.error(f"ツイートに失敗しました。{e}")


class TwitterHandler(BaseHandler):
    def __init__(self, video):
        super().__init__(video)
        self._client = Client()

    def __call__(self, message):
        at = message.published_at_jst().strftime("%Y-%m-%d %H:%M:%S")
        text = (
            f"{at}、「{self.video.title}」に{self.video.channel.owner_name}が現れました。"
            f"{self.video.url}"
        )
        self._client.tweet(text)
