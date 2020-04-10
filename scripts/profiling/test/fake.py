# fake script for profiling test
import random

# to profile this script
# kernprof -l fake.py

# run this to read results
# python -m line_profiler fake.py.lprof

@profile
def do_stuff(numbers):
    s = sum(numbers)
    l = [numbers[i]/43 for i in range(len(numbers))]
    m = ['hello'+str(numbers[i]) for i in range(len(numbers))]

numbers = [random.randint(1,100) for i in range(1000)]
print(numbers)
