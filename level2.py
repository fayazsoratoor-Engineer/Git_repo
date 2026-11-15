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