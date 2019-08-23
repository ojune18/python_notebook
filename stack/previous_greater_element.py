from stack import Stack


def previous_greater_elem(arr):
    s = Stack()

    for item in arr:

        if s.isEmpty():
            print(-1, end=" ")
            s.push(item)
        else:

            if s.peek() > item:
                print(s.peek(), end=" ")
            elif s.peek() <= item:

                while not s.isEmpty() and s.peek() < item:
                    s.pop()

                if s.isEmpty():
                    print(-1, end=" ")
                    s.push(item)
                else:
                    print(s.peek(), end=" ")


previous_greater_elem([10,4,2,20,40, 12 , 30])