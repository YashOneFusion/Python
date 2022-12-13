arr = [4,5,1,3,45,23,5,3,8]
for i in range(len(arr)):
    for j in range(0, (len(arr)-i-1)):
        if arr[j+1] < arr[j]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)
