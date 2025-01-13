from matplotlib import pyplot as plt


bub_file = open("bubSort.txt")
contents = bub_file.read()
contents = contents.split(" ns\n")
contents.pop()
bsort = []
for i in contents:
    bsort.append(int(i)//1000)

runs = list(range(1, len(bsort) + 1))


sel_file = open("selSort.txt")
contents = sel_file.read()
contents = contents.split(" ns\n")
contents.pop()
ssort = []
for i in contents:
    ssort.append(int(i)//1000)

runs = list(range(1, len(ssort) + 1))



plt.plot(runs, bsort, label="Bubble Sort Swaps", marker ="o")
plt.plot(runs, ssort, label="Selection Sort Swaps", marker='x')
plt.xlabel("Run Number")
plt.ylabel("Time Taken (*1000) ns")
plt.title("Comparison of Bubble Sort and Selection Sort")
plt.legend()
plt.grid()
plt.show()