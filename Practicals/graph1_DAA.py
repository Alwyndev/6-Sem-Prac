from matplotlib import pyplot as plt

if __name__ == "__main__":  

    bub_file = open("bubbleSortTimes.txt")
    contents = bub_file.read()
    contents = contents.split(" ns\n")
    contents.pop()
    bsort = []
    runs = []
    for i in contents:
        i = i.split(":")
        runs.append(i[0])
        bsort.append(int(i[1])//1000)


    sel_file = open("selectionSortTimes.txt")
    contents = sel_file.read()
    contents = contents.split(" ns\n")
    contents.pop()
    ssort = []
    for i in contents:
        i=i.split(":")
        ssort.append(int(i[1])//1000)



    plt.plot(runs, bsort, label="Bubble Sort Swaps", marker ="o")
    plt.plot(runs, ssort, label="Selection Sort Swaps", marker='x')
    plt.xlabel("Run Number")
    plt.ylabel("Time Taken (*1000) ns")
    plt.title("Comparison of Bubble Sort and Selection Sort")
    plt.legend()
    plt.grid()
    plt.show()