from my_counter_lib.generators import counter_generator
from my_counter_lib.timers import timeout_counter

counter = counter_generator(1)

timer = timeout_counter(1, counter)


def my_test_function(
    first_long_argument, second_long_argument, third_long_argument, fourth_long_argument
):
    pass
