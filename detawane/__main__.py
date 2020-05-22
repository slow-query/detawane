import os
import sys
import signal
import time
from .logger import get_local_logger
from argparse import ArgumentParser
from .video_list import VideoList
from .chat import build_processor

parser = ArgumentParser()
parser.add_argument('file', type=str, help='channel list file')
args = parser.parse_args()

logger = get_local_logger(__name__)

processors = []
for video in VideoList.load(args.file):
    processors.append(
        build_processor(video)
    )
    logger.info(f'{video.channel.owner_name}の「{video.title}」の監視を開始しました。')

def terminate(num, frame):
    processors.clear()
    sys.exit()

signal.signal(signal.SIGINT, terminate)
signal.signal(signal.SIGTERM, terminate)

while True:
    for processor in processors:
        processor.process()
    time.sleep(5)
