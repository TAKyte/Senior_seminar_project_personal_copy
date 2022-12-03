# Thomas Kyte
# senior seminar

"""
Currently the timing functions are commented out to calculate runtimes please uncomment the imports and the function
calls in this main file

This program calculates the time taken to generate different lengths of random numbers using the linear congruential
lagged Fibonacci and middle square methods. it also uses chi squared method to determine the difference in output vs.
expected output aka random output. The times output to a file that has the seed number followed by _avg_times.
the chi squared values can be found in a file named seed#all_avg the %coverage can also be found in this file

graphs are also generated based on the frequencies of each number and are saved as a png. if this is undesired it
can be commented out in the chi_occurences file
"""

# import functions from helper files
from linear_congruential import lin_con
from lag_fib import lag_fib
from mdl_sqr import mdl_sqr
from chi_occ import chi_occ
# from calc_times import calc_times
# from gen_times import gen_times

if __name__ == '__main__':
    # list of seeds used to get comparison data
    # seed one = 11111111
    # seed two = 26857536
    # seed three = 39991234
    # seed four = 57224956

    # active seed for testing
    seed = 59617645
    # range of random numbers to generate is 0 to (prng_r-1)
    prng_r = 501
    # # clear all previous output data
    open('lin_100.txt', 'w').close()
    open('lin_1000.txt', 'w').close()
    open('lin_10000.txt', 'w').close()
    open('lin_10000000.txt', 'w').close()

    open('lag_100.txt', 'w').close()
    open('lag_1000.txt', 'w').close()
    open('lag_10000.txt', 'w').close()
    open('lag_10000000.txt', 'w').close()

    open('mdl_100.txt', 'w').close()
    open('mdl_1000.txt', 'w').close()
    open('mdl_10000.txt', 'w').close()
    open('mdl_10000000.txt', 'w').close()

    # output all prng array to txt files
    # the structure is as follows
    # result = method(active seed, size of random number array,
    # take the array of results and append to file (probably should have written directly to file)
    # close the output file after all numbers have been appended
#######################################################################################################################
    res = lin_con(seed, 100, prng_r)
    output = open('lin_100_O.txt', 'w')
    for i in res:
        output.write(str(i) + "\n")
    output.close()

    res = lag_fib(seed, 100, prng_r)
    output = open('lag_100_O.txt', 'w')
    for i in res:
        output.write(str(i) + "\n")
    output.close()

    res = mdl_sqr(seed, 100, prng_r)
    output = open('mdl_100_O.txt', 'w')
    for i in res:
        output.write(str(i) + "\n")
    output.close()

    res = lin_con(seed, 1000, prng_r)
    output = open('lin_1000_O.txt', 'w')
    for i in res:
        output.write(str(i) + "\n")
    output.close()

    res = lag_fib(seed, 1000, prng_r)
    output = open('lag_1000_O.txt', 'w')
    for i in res:
        output.write(str(i) + "\n")
    output.close()

    res = mdl_sqr(seed, 1000, prng_r)
    output = open('mdl_1000_O.txt', 'w')
    for i in res:
        output.write(str(i) + "\n")
    output.close()

    res = lin_con(seed, 10000, prng_r)
    output = open('lin_10000_O.txt', 'w')
    for i in res:
        output.write(str(i) + "\n")
    output.close()

    res = lag_fib(seed, 10000, prng_r)
    output = open('lag_10000_O.txt', 'w')
    for i in res:
        output.write(str(i) + "\n")
    output.close()

    res = mdl_sqr(seed, 10000, prng_r)
    output = open('mdl_10000_O.txt', 'w')
    for i in res:
        output.write(str(i) + "\n")
    output.close()

    res = lin_con(seed, 10000000, prng_r)
    output = open('lin_10000000_O.txt', 'w')
    for i in res:
        output.write(str(i) + "\n")
    output.close()

    res = lag_fib(seed, 10000000, prng_r)
    output = open('lag_10000000_O.txt', 'w')
    for i in res:
        output.write(str(i) + "\n")
    output.close()

    res = mdl_sqr(seed, 10000000, prng_r)
    output = open('mdl_10000000_O.txt', 'w')
    for i in res:
        output.write(str(i) + "\n")
    output.close()
#######################################################################################################################
    # generate times for 50 runs of each method
    # gen_times(seed, prng_r)

    # call the times function to calculate averages from above data
    # calc_times(seed)

    # # call chi occurrences function to get the average occurrences of each function
    chi_occ("lin", "100", prng_r, seed)
    chi_occ("lin", "1000", prng_r, seed)
    chi_occ("lin", "10000", prng_r, seed)
    chi_occ("lin", "10000000", prng_r, seed)

    chi_occ("lag", "100", prng_r, seed)
    chi_occ("lag", "1000", prng_r, seed)
    chi_occ("lag", "10000", prng_r, seed)
    chi_occ("lag", "10000000", prng_r, seed)

    chi_occ("mdl", "100", prng_r, seed)
    chi_occ("mdl", "1000", prng_r, seed)
    chi_occ("mdl", "10000", prng_r, seed)
    chi_occ("mdl", "10000000", prng_r, seed)
