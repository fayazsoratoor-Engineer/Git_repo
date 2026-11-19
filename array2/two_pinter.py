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