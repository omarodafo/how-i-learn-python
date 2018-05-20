from random import randint

arr = []

for i in range(0,9):
    pseudo_number = randint(0,999)
    arr.append(pseudo_number)

print(arr)

for i in range(0, len(arr)):
    for j in range(len(arr)-1,i,-1):
        if arr[j]<arr[j-1]:
            arr[j-1],arr[j] = arr[j],arr[j-1]

print(arr)