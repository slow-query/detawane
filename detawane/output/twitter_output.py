import os
import tweepy
from .base_output import BaseOutput

class Client:
    def __init__(self):
        auth = tweepy.OAuthHandler(os.environ['TWITTER_CONSUMER_KEY'], os.environ['TWITTER_CONSUMER_SECRET'])
        auth.set_access_token(os.environ['TWITTER_ACCESS_KEY'], os.environ['TWITTER_ACCESS_SECRET'])
        self.api = tweepy.API(auth)

    def tweet(self, text):
        self.api.update_status(text)

class TwitterOutput(BaseOutput):
    CLIENT = Client()

    def __init__(self, video):
        super().__init__(video)

    def __call__(self, message):
        print('[{}][{}][{}] {}'.format(self.video.channel.owner_name, str(message.published_at), message.name, message.text))
        text = '{}が「{}」に現れました。 {}'.format(self.video.channel.owner_name, self.video.title, self.video.url)
        self.CLIENT.tweet(text)
