from .base_output import BaseOutput

class StdoutOutput(BaseOutput):
    def __call__(self, message):
        print('[{}][{}] {}'.format(self.video.channel.owner_name, message.name, message.text))
