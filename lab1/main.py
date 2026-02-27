import time
from typing import Iterator


def counter_generator(start_value: int) -> Iterator[int]:
    current_value = start_value

    while True:
        yield current_value
        current_value += 1


def timeout_counter(duration: float, iterator: Iterator[int]):
    stop_time = time.time() + duration

    while stop_time > time.time():
        print(next(iterator))


counter = counter_generator(1)
timeout_counter(1, counter)


