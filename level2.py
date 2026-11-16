arr=[2,1,2,1,3,4,5,1,1,2]
sets=set(arr)
print(list(sets))

#OR

arr=[2,1,2,1,3,4,5,1,1,2]
unique_arr=[]
for i in arr:
    if i not in unique_arr:
        unique_arr.append(i)
print(unique_arr)


#zero to hh end of the array
arr=[2,1,0,2,0,1,3,0,4,5,0,1,1,2]
counts=arr.count(0)
for i in arr:
    if i == 0:
        arr.remove(0)
arr += [0] * counts
print(arr)

arr=[2,1,0,2,0,1,3,0,4,5,0,1,1,2]
counts=arr.count(0)
for i in arr:
    if i == 0:
        arr.remove(0)
zero=[0] * counts
zero+=arr
print(zero)


#left rotate the array by k times
arr = [1, 2, 3, 4, 5]

first = arr[0]

for i in range(len(arr) - 1):
    arr[i] = arr[i + 1]

arr[-1] = first

print(arr)
arr = [1, 2, 3, 4, 5]
large = arr[0]
second = arr[0]

for i in range(len(arr)):
    if arr[i] > large:
        second = large
        large = arr[i]
    elif arr[i] > second and arr[i] != large:
        second = arr[i]

print("Largest:", large)
print("Second Largest:", second)


#merge two sorted arrays
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merged = []
i,j=0,0
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        merged.append(arr1[i])
        i += 1
    else:
        merged.append(arr2[j])
        j += 1
print(merged + arr1[i:] + arr2[j:])a