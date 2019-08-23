def insertion_sort(arr):
    i = 1
    while i < len(arr):
        if arr[i] < arr[i - 1]:
            j = i - 1
            key = arr[i]
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]

                j -= 1
            arr[j+1] = key
        i += 1

    print("Array is => ", arr)


insertion_sort([4, 0, 1, 9, 67, 34, 8, 39, 60])
