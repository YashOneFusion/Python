#Return Product of elements in an array
arr = [6,2,5,3,2,4,3,4,4,5]
product=0
for _ in range(len(arr)-1):
    if product==0:
        product=arr[_]
    product*=arr[_+1]
print(product)