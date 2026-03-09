import time
from typing import Iterator


def timeout_counter(duration: float, iterator: Iterator[int]):
    stop_time = time.time() + duration

    while stop_time > time.time():
        print(next(iterator))
