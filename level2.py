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

arr=[2,1,0,2,0,1,3,0,4,5,0,1,1,2]
counts=arr.count(0)
for i in arr:
    if i == 0:
        arr.remove(0)
arr += [0] * counts
print(arr)