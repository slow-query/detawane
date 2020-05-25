from argparse import ArgumentParser

from .chat import build_processor
from .cli.runner import Runner
from .video_list import VideoList

parser = ArgumentParser()
parser.add_argument(
    "--file", "-f", type=str, required=True, help="specify channel list file"
)
parser.add_argument(
    "--adapter",
    "-a",
    type=str,
    default="pychat",
    metavar="ADAPTER_TYPE",
    help="select either pychat or api",
)
args = parser.parse_args()

processors = []
for video in VideoList.load(args.file):
    processors.append(build_processor(args.adapter, video))


runner = Runner()
runner.run(processors)
