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

def merge_sorted_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    return merged + arr1[i:] + arr2[j:]


def merge_sorted_arrays_sorted(arr1, arr2):
    return sorted(arr1 + arr2)