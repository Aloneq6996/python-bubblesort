arr = [8, 2, 1, 9, 5]
n = len(arr)
for i in range(n):
    for j in range(n - 1):
        if arr[j] > arr[j+1]:
            arr[j+1], arr[j] = arr[j], arr[j+1]
print(arr)