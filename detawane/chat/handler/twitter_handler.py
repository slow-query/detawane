import os
import tweepy
from .base_handler import BaseHandler


class Client:
    def __init__(self):
        auth = tweepy.OAuthHandler(
            os.environ["TWITTER_CONSUMER_KEY"], os.environ["TWITTER_CONSUMER_SECRET"]
        )
        auth.set_access_token(
            os.environ["TWITTER_ACCESS_KEY"], os.environ["TWITTER_ACCESS_SECRET"]
        )
        self.api = tweepy.API(auth)

    def tweet(self, text):
        self.api.update_status(text)


class TwitterHandler(BaseHandler):
    CLIENT = Client()

    def __init__(self, video):
        super().__init__(video)

    def __call__(self, message):
        text = f"{self.video.channel.owner_name}が「{self.video.title}」に現れました。 {self.video.url}"
        self.CLIENT.tweet(text)
