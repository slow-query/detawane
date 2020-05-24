import signal
import time
from argparse import ArgumentParser

from .chat import build_processor
from .logger import get_local_logger
from .video_list import VideoList

parser = ArgumentParser()
parser.add_argument("file", type=str, help="channel list file")
args = parser.parse_args()

logger = get_local_logger(__name__)

is_running = True
processors = []
for video in VideoList.load(args.file):
    processors.append(build_processor(video))
    logger.info(f"{video.channel.owner_name}の「{video.title}」の監視を開始しました。")


def terminate(num, frame):
    global is_running
    is_running = False


signal.signal(signal.SIGINT, terminate)
signal.signal(signal.SIGTERM, terminate)

while is_running:
    for processor in processors:
        processor.process()
    time.sleep(5)

for processor in processors:
    video = processor.video
    processor.terminate()
    logger.info(f"{video.channel.owner_name}の「{video.title}」の監視を終了しました。")
