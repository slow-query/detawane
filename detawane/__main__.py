from .chat import build_processor
from .cli.config import Config
from .cli.runner import Runner

config = Config()

processors = []
for video in config.videos:
    processors.append(build_processor(video, config.adapter))

runner = Runner()
runner.run(processors)
