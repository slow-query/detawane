from .base_handler import BaseHandler


class StdoutHandler(BaseHandler):
    def __call__(self, message):
        print(
            "[{}][{}] {}".format(
                self.video.channel.owner_name, message.name, message.text
            ),
            flush=True,
        )
