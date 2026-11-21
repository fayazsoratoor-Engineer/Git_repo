array=[5, 10, 15, 20]
left=array[0]
right=len(array)-1

while left <right:

    array[left], array[right] = array[right], array[left]
    left += 1
    right -= 1


def sums(arr,k):
    left=0
    right=len(arr)-1
    while left < right:
        current_sum=arr[left]+arr[right]
        if current_sum==k:
            return arr[left], arr[right]
        elif current_sum<k:
            left+=1
        else:
            right-=1
    return False

print(sums([1,2,3,4,5],7))

def move_zero(arr):
    left=0
    right=len(arr)-1
    while left <right:
        if arr[left]==0 and arr[right]!=0:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        elif arr[left]!=0:
            left+=1
        elif arr[right]==0:
            right-=1
    return arr
print(move_zero([0,1,0,3,12]))

print("Fayaz")
for i in range(10):
    print(i)
    if i==10:
        continue
def reverse_string(s):
    left=0
    right=len(s)-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return s

def reverse_string(s):
    left=0
    right=len(s)-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return s

def point(arr):
    left=0
    right=len(arr)-1
    while left<right:
        if arr[left]==0 and arr[right]!=0:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        elif arr[left]!=0:
            left+=1
        elif arr[right]==0:
            right-=1
    return arr