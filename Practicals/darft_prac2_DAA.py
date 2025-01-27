from matplotlib import pyplot as plt

if __name__ == "__main__":  

    bub_file = open("insertionSortTimes.txt")
    contents = bub_file.read()
    contents = contents.split(" ns\n")
    contents.pop()
    isort = []
    for i in contents:
        isort.append(int(i)//100)

    runs = list(range(1, len(isort) + 1))


    sel_file = open("mergeSortTimes.txt")
    contents = sel_file.read()
    contents = contents.split(" ns\n")
    contents.pop()
    msort = []
    for i in contents:
        msort.append(int(i)//100)

    runs = list(range(1, len(msort) + 1))



    plt.plot(runs, isort, label="Insertion Sort Swaps", marker ="o")
    plt.plot(runs, msort, label="Merge Sort Swaps", marker='x')
    plt.xlabel("Run Number")
    plt.ylabel("Time Taken (*100) ns")
    plt.title("Comparison of Merge Sort and Insertion Sort")
    plt.legend()
    plt.grid()
    plt.show()