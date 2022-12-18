from contextlib import contextmanager
import time


class cm_timer_1():

    def __init__(self):
        self.start_tm = None

    def __enter__(self):
        self.start_tm = time.time()
        return self

    def __exit__(self, exp_type, exp_value, traceback):  # для обработки исключений
        print(time.time() - self.start_tm)


@contextmanager
def cm_timer_2():
    start = time.time()
    yield
    print(time.time() - start)