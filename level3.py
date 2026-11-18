print("fayazsoratoor")

def add(a, b):
    return a + b
def largest(arr):
    large = arr[0]
    for i in arr:
        if i > large:
            large = i
    return large

def second_largest(arr):
    large = arr[0]
    second = arr[0]

    for i in range(len(arr)):
        if arr[i] > large:
            second = large
            large = arr[i]
        elif arr[i] > second and arr[i] != large:
            second = arr[i]

    return second