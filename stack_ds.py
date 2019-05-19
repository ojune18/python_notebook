def stack_sorter():
    arr = [1, 5, 2, 0, 12, 3, 8, 4, 80, 101, 32, 19, 43, 20]
    sorted_stack = []
    temp = []

    for item in arr:
        if len(sorted_stack) == 0:
            sorted_stack.append(item)

        else:
            if item >= sorted_stack[len(sorted_stack) - 1]:
                sorted_stack.append(item)
            else:
                while len(sorted_stack) > 0 and sorted_stack[len(sorted_stack) - 1] > item:
                    temp.append(sorted_stack.pop())

                sorted_stack.append(item)
                while len(temp) > 0:
                    sorted_stack.append(temp.pop())


    print(sorted_stack)

stack_sorter()
