import os
import sys
import signal
import time
from argparse import ArgumentParser
from .chat_watcher import ChatWatcher
from .video_list import VideoList
from .output.stdout_output import StdoutOutput
from .output.twitter_output import TwitterOutput

parser = ArgumentParser()
parser.add_argument('file', type=str, help='channel list file')
args = parser.parse_args()

watchers = []
for video in VideoList.load(args.file):
  watchers.append(
      ChatWatcher(video = video, output_class = TwitterOutput)
  )
  print('{}の「{}」の監視を開始しました。'.format(video.channel.owner_name, video.title))

def terminate(num, frame):
    for watcher in watchers:
        watcher.terminate()
    sys.exit()

signal.signal(signal.SIGINT, terminate)
signal.signal(signal.SIGTERM, terminate)

while True:
  time.sleep(1)
