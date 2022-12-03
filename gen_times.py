# import PRNG methods
from linear_congruential import lin_con
from lag_fib import lag_fib
from mdl_sqr import mdl_sqr

# import time module for time comparison
import time


def gen_times(seed, prng_r):
    # basic structure is as follows
    # get start time
    # result = method(active seed, size to generate, range of output)
    # save time taken to generate numbers
    # append that time to the time taken file

    for x in range(50):
        # call all 100 length prng
        print("100 len")

        startTime = time.time()
        res = lin_con(seed, 100, prng_r)
        time_process = str((time.time() - startTime))
        output = open('lin_100.txt', 'a')
        output.write(time_process)
        output.write("\n")
        output.close()

        startTime = time.time()
        res = lag_fib(seed, 100, prng_r)
        time_process = str((time.time() - startTime))
        output = open('lag_100.txt', 'a')
        output.write(time_process)
        output.write("\n")
        output.close()

        startTime = time.time()
        res = mdl_sqr(seed, 100, prng_r)
        time_process = str((time.time() - startTime))
        output = open('mdl_100.txt', 'a')
        output.write(time_process)
        output.write("\n")
        output.close()

        # call all 1000 length prng
        print("1000 len")

        startTime = time.time()
        res = lin_con(seed, 1000, prng_r)
        time_process = str((time.time() - startTime))
        output = open('lin_1000.txt', 'a')
        output.write(time_process)
        output.write("\n")
        output.close()

        startTime = time.time()
        res = lag_fib(seed, 1000, prng_r)
        time_process = str((time.time() - startTime))
        output = open('lag_1000.txt', 'a')
        output.write(time_process)
        output.write("\n")
        output.close()

        startTime = time.time()
        res = mdl_sqr(seed, 1000, prng_r)
        time_process = str((time.time() - startTime))
        output = open('mdl_1000.txt', 'a')
        output.write(time_process)
        output.write("\n")
        output.close()

        # call all 10000 length prng
        print("10000 len")

        startTime = time.time()
        res = lin_con(seed, 10000, prng_r)
        time_process = str((time.time() - startTime))
        output = open('lin_10000.txt', 'a')
        output.write(time_process)
        output.write("\n")
        output.close()

        startTime = time.time()
        res = lag_fib(seed, 10000, prng_r)
        time_process = str((time.time() - startTime))
        output = open('lag_10000.txt', 'a')
        output.write(time_process)
        output.write("\n")
        output.close()

        startTime = time.time()
        res = mdl_sqr(seed, 10000, prng_r)
        time_process = str((time.time() - startTime))
        output = open('mdl_10000.txt', 'a')
        output.write(time_process)
        output.write("\n")
        output.close()

        # call all 100000000 length prng
        print("10000000 len")

        startTime = time.time()
        res = lin_con(seed, 10000000, prng_r)
        time_process = str((time.time() - startTime))
        output = open('lin_10000000.txt', 'a')
        output.write(time_process)
        output.write("\n")
        output.close()

        startTime = time.time()
        res = lag_fib(seed, 10000000, prng_r)
        time_process = str((time.time() - startTime))
        output = open('lag_10000000.txt', 'a')
        output.write(time_process)
        output.write("\n")
        output.close()

        startTime = time.time()
        res = mdl_sqr(seed, 10000000, prng_r)
        time_process = str((time.time() - startTime))
        output = open('mdl_10000000.txt', 'a')
        output.write(time_process)
        output.write("\n")
        output.close()
