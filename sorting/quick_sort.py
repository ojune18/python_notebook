import math

"""
Never Use quicksort for nearly sorted arrays
We would end up in doing probably O(n2) iterations in that case
"""


def quick_sort(arr, l, r):
    index_to_partition = partition(arr, l, r)

    if l < index_to_partition - 1:
        quick_sort(arr, l, index_to_partition - 1)

    if index_to_partition < r:
        quick_sort(arr, index_to_partition , r)

    return arr


def partition(arr, left, right):
    pivot = (left + right) // 2

    i = left
    j = right

    while i <= j:

        while arr[i] < arr[pivot]:
            i += 1

        while arr[j] > arr[pivot]:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    return i


arr = [19, 22, 63, 105, 2, 46]

print(quick_sort(arr, 0, len(arr) - 1))


