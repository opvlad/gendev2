from my_counter_lib.generators import counter_generator
from my_counter_lib.timers import timeout_counter

counter = counter_generator(1)

timer = timeout_counter(1, counter)
