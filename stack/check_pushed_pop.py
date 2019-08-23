def pushed_pop(arr1, arr2):
    s = len(arr1) - 1

    for i in range(len(arr1) - 1):
        if arr1[i] != arr2[s - i]:
            return False

    return True


print(pushed_pop([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
