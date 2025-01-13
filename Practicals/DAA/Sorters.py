import random as r
import matplotlib.pyplot as plt

def bubbleSort(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
                count += 1
    return count

def selectSort(nums):
    count = 0
    for i in range(len(nums)):
        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        if min_idx != i:
            temp = nums[i]
            nums[i] = nums[min_idx]
            nums[min_idx] = temp
            count += 1
    return count

if __name__ == "__main__":
    low_lim = int(input("Enter the lower limit  :  "))
    upp_lim = int(input("Enter the upper limit  :  "))
    lim = int(input("Enter the number of numbers :  "))
    count = int(input("Enter the number of times to run  :  "))

    bubsort = []
    selsort = []

    for _ in range(count):
        nums = [r.randint(low_lim, upp_lim) for _ in range(lim)]
        nums2 = nums[:]
        bubsort.append(bubbleSort(nums))
        selsort.append(selectSort(nums2))

    runs = list(range(1, count + 1))

    print(f"{bubsort}\n{selsort}")

   