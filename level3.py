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

def merge_sorted_arrays_sorted_with_key(arr1, arr2):
    return sorted(arr1 + arr2, key=lambda x: x)

def print_hello_world():
    print("Hello World")
    print("Fayaz")

def print_hello_world_multiple_times(n):
    for _ in range(n):
        print("Hello World")

def add_numbers(a, b):
    return a + b

def find_largest(arr):
    large = arr[0]
    for i in arr:
        if i > large:
            large = i
    return large

def find_second_largest(arr):
    large = arr[0]
    second = arr[0]
    for i in arr:
        if i > large:
            second = large
            large = i
        elif i > second and i != large:
            second = i
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

def palindrome_check(s):
    return s == s[::-1]

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = [0, 1]
        for i in range(2, n):
            next_fib = fib_seq[i - 1] + fib_seq[i - 2]
            fib_seq.append(next_fib)
        return fib_seq

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True