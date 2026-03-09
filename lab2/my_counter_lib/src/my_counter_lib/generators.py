from typing import Iterator


def counter_generator(start_value: int) -> Iterator[int]:
    current_value = start_value

    while True:
        yield current_value
        current_value += 1
