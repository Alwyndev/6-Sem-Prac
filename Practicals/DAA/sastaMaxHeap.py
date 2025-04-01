arr = list(map(int, input().split()))

for i in range(len(arr)):
    temp = arr[i]
    max_el = max(arr)
    if max_el >= arr[i]:
        idx = arr.index(max_el)
        