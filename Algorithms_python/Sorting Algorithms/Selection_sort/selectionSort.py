arr = [4,5,1,3,45,23,5,3,8]
n = len(arr)
for i in range(n):
		minimum_index = i
		for j in range(i+1, n):
				if arr[j] < arr[minimum_index]:
					minimum_index = j
					j += 1
		arr[i], arr[minimum_index] = arr[minimum_index], arr[i] #swap

print("Sorted array:")
for i in range(len(arr)):
	print(arr[i])