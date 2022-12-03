def calc_times(s):
    # open a file
    f = open(str(s) + "_avg_times.txt", 'w')
    # array of all generator types
    t = ['lin', 'lag', 'mdl']
    # array with all output sizes
    siz = ['100', '1000', '10000', '10000000']

    # for all types and sizes in type
    # open a second file
    # sum all times in file and divide by the number of generations ran
    # output the average time to the f file
    # close f1
    # close f after all types and sizes finished
    for i in t:
        for j in siz:
            f1 = open(i + "_" + j + ".txt", 'r')
            total = 0
            tnum = 0
            for line in f1:
                total = total + float(line.strip())
                tnum = tnum + 1
            f.write(i + "_" + j + "\n")
            if total > 0:
                f.write(str(total / tnum) + "\n")
            else:
                f.write("0 \n")
            f1.close()
    f.close()
