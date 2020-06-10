import time


def keep_time(second=0):
    return TimeKeeper(second)


class TimeKeeper:
    def __init__(self, waiting_second):
        self.waiting_second = waiting_second

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        remaining_time = self.waiting_second - (time.time() - self.start_time)
        time.sleep(remaining_time if remaining_time > 0 else 0)

    def set_waiting_second(self, second):
        self.waiting_second = second
