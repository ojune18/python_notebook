from stack import Stack

"""
This is not YET complete. I would have to write this again.
"""

def remove_overlapping_series(series):
    s = Stack()

    for item in series:


        if s.isEmpty():
            s.push(item)
        else:
            top = s.peek()
            if top[0] <= item[0] and top[1] >= item[1]:
                continue;
            else:

                while top[0] > item[0] and top[1] < item[1]:
                    s.pop()
                    if s.isEmpty():
                        break
                    else:
                        top = s.peek()
                s.push(item)

    print(s)


remove_overlapping_series([(9, 11), (3, 7), (2, 4), (5, 7), (8, 10)])
