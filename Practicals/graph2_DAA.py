from matplotlib import pyplot as plt

if __name__ == "__main__":  

    ins_file = open("insertionSortTimes.txt")
    contents = ins_file.read()
    contents = contents.split(" ns\n")
    contents.pop()
    runs = []
    isort = []
    for i in contents:
        i=i.split(":")
        runs.append(int(i[0]))
        isort.append(int(i[1])//1000)
    
    mer_file = open("mergeSortTimes.txt")
    contents = mer_file.read()
    contents = contents.split(" ns\n")
    contents.pop()
    msort = []
    for i in contents:
        i=i.split(":")
        msort.append(int(i[1])//1000)


    plt.plot(runs, isort, label="Insertion Sort Swaps", marker ="o")
    plt.plot(runs, msort, label="Merge Sort Swaps", marker='x')
    plt.xlabel("Run Number")
    plt.ylabel("Time Taken (*1000) ns")
    plt.title("Comparison of Merge Sort and Insertion Sort")
    plt.legend()
    plt.grid()
    plt.show()