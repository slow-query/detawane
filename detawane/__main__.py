from .chat import build_processor
from .chat.sentry_processor import SentryProcessor
from .cli.config import Config
from .cli.runner import Runner

config = Config()

processors = [SentryProcessor()]
for video in config.videos:
    processors.append(build_processor(video, config.adapter))

runner = Runner()
runner.run(processors)
