import os
import sys
import signal
import time
from .logger import get_local_logger
from argparse import ArgumentParser
from .chat_watcher import ChatWatcher
from .video_list import VideoList
from .output.stdout_output import StdoutOutput
from .output.twitter_output import TwitterOutput

parser = ArgumentParser()
parser.add_argument('file', type=str, help='channel list file')
args = parser.parse_args()

logger = get_local_logger(__name__)

watchers = []
for video in VideoList.load(args.file):
  watchers.append(
      ChatWatcher(video = video, output_class = TwitterOutput)
  )
  logger.info(f'{video.channel.owner_name}の「{video.title}」の監視を開始しました。')

def terminate(num, frame):
    watchers.clear()
    sys.exit()

signal.signal(signal.SIGINT, terminate)
signal.signal(signal.SIGTERM, terminate)

while True:
  time.sleep(1)
