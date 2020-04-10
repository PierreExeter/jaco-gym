import cProfile
import re
import pstats
from line_profiler import LineProfiler
import random

# prog = re.compile("pierre")
# result = prog.match("yolo")

# print(prog)
# print(result)

#######################

# cProfile.run('re.compile("foo|bar")')

# profile and save stats in file restats
cProfile.run('re.compile("foo|bar")', 'restats')

# load file restat
p = pstats.Stats('restats')

# print stats
p.strip_dirs().sort_stats(-1).print_stats()

# p.sort_stats('name')
# p.print_stats()

# p.sort_stats('cumulative').print_stats(10)

####################33

# def main():

#     def do_stuff(numbers):
#         s = sum(numbers)
#         l = [numbers[i]/43 for i in range(len(numbers))]
#         m = ['hello'+str(numbers[i]) for i in range(len(numbers))]

#     numbers = [random.randint(1,100) for i in range(1000)]


# if __name__ == "__main__": 
#     main()


# lp = LineProfiler()
# lp_wrapper = lp(main)
# # lp_wrapper(numbers)
# lp.print_stats()


#############33


# def do_stuff(numbers):
#     s = sum(numbers)
#     l = [numbers[i]/43 for i in range(len(numbers))]
#     m = ['hello'+str(numbers[i]) for i in range(len(numbers))]

# numbers = [random.randint(1,100) for i in range(1000)]


# lp = LineProfiler()
# lp_wrapper = lp(do_stuff)
# lp_wrapper(numbers)
# lp.print_stats()