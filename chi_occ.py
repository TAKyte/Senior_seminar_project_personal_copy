# Thomas Kyte
# this function reads through the output and generates an array based on the number of occurrences of each number
# import python math, scientipi calculations, and graphing tool
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


# finds the occurrences of each number, the number of unique values, and determine if the distribution of numbers is
# significantly different than whats expected
def chi_occ(t, s, prng_r, seed):
    # array that will contain the occurrences of each number generated
    occurrences = []

    # array used for graphing holds each value in range generated
    x = []

    # for each number in the range possible set the starting number of occurrences to zero
    for i in range(prng_r):
        occurrences.append(0)
        x.append(i)

    # open a file and read in all values to occurrence array then close the file
    f = open(t + "_" + s + "_O" + ".txt", 'r')
    for line in f:
        num = int(line.strip())
        occurrences[num] = occurrences[num] + 1
    f.close()

    # open a file and write into it the number of occurrences of each number followed by what number it is
    f = open(t + "_" + s + "_AVG" + ".txt", 'w')
    f.write("occurrences \n")
    # how many occurences there is of the most frequently generated number is stored in maxv
    maxv = 0
    # will contain the number of unique values
    unique_num = 0

    # loop through array updating maxv and unique numbers
    for i in range(len(occurrences)):
        if occurrences[i] >= 1:
            unique_num = unique_num + 1
        if occurrences[i] > maxv:
            maxv = occurrences[i]
        # output data to the file and put a new line after
        f.write(str(occurrences[i]) + " occurrences of " + str(i))
        f.write("\n")
    f.close()

    # graphing
    # y is the axes for the frequency of each number
    # is is above and is 0 - max val possible to generate
    y = occurrences
    # set dimensions of graph
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    # auto set bar spacing I believe
    plt.rcParams["figure.autolayout"] = True
    # use multiple bar colors to make different data points move visible
    plt.bar(x, y, color=['red', 'green', 'blue', 'cyan', 'purple', 'gold'])
    # set the title of the graph and increase the font size to be easier to read
    plt.title(t + "_" + s + " frequencies", fontsize=20)
    # set x and y data labels
    plt.xlabel('value')
    plt.ylabel('# of occurrences')
    # set y axis size to 1.2 times the highest occurrence number so its easier to see small differences in the most
    # common outputs
    plt.ylim(top=maxv * 1.2)
    plt.grid(axis='y')
    # force all x values to be graphed with data labels every 100 values
    plt.xticks(np.arange(0, 500, 100))
    # only need one or the other of below statements at any given time with other commented out
    # save the figure as a png file
    plt.savefig(str(seed) + "_" + t + "_" + s + " frequencies.png")
    # show the plot in the ide
    plt.show()

    # open an all averages file, print the results of scipi chi squared and the number of unique occurrences and the
    # present of the possible range covered by the generator. the better the generator the closer to 100% the result
    # is for generation sizes bigger than the output range
    f = open(str(seed) + "all_AVG" + ".txt", 'a')
    f.write(str(seed) + "_" + t + "_" + s + "_AVG\n")
    f.write(str(stats.chisquare(occurrences)) + "\n")
    f.write("Unique numbers generated: " + str(unique_num) + "\n")
    f.write("The present of possible output covered is: " + str('{:.2%}'.format(unique_num / prng_r)) + "\n")
