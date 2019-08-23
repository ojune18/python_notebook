def draw_game():
    n = int(input("Enter a Number :\t"))
    i = n
    s1 = " {}".format("-" * i)
    s = "|{}".format(" " * i)
    while n > 0:
        print(s1 * i, end=" \n")
        print(s * i, end="|\n")
        n -= 1
    print(s1 * i, end=" ")


# draw_game()

def design_dict():
    d = {"Input": 'Vivek', 'Output': "Muneer", "Run": "Avi", "Magic": 'Vivek', "Test": 'Vivek', "Bug": "Avi"}

    op = {}

    for k, v in d.items():
        op[v] = op.get(v, [])
        op[v].append(k)

    print(op)


# design_dict()

def find_smallest_largest(arr):
    min_num = arr[0]
    max_num = arr[0]

    # return min(arr), max(arr)

    for item in arr:

        if item > max_num:
            max_num = item

        elif item < min_num:
            min_num = item

    return min_num, max_num


# print(find_smallest_largest([1, 7, 2, 9, 6, 13, 4, 3, 5]))

def find_pair(arr, num):
    d = {}
    count = 0

    for item in arr:
        if d.get(num - item, None) and not d[num - item] == item:
            d[num - item] = item
            count += 1
        else:
            d[item] = 's'

    return count


def find_pair_memory_optimized(arr, num):
    arr = sorted(arr)
    j = len(arr) - 1
    i = 0

    while i < j:
        if arr[i] + arr[j] > num:
            j -= 1
        elif arr[i] + arr[j] < num:
            i += 1
        else:
            print(arr[i], " +  ", arr[j])
            i += 1
            j -= 1

    return 'OK'


print(find_pair_memory_optimized([0, 14, 0, 4, 7, 8, 3, 5, 7, 11], 11))


def printRepeating(arr, size):
    print("The repeating elements are: ")

    for i in range(0, size):

        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            print(abs(arr[i]), end=" ")


arr = [1, 8, 3, 1, 3, 6, 6]
arr_size = len(arr)

#printRepeating(arr, arr_size)




