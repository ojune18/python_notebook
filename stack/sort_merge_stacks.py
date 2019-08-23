from stack import Stack


def merge_stacks(s1: Stack, s2: Stack):
    s = Stack()

    while not s1.isEmpty() or not s2.isEmpty():

        arr = []

        if not s1.isEmpty():
            t1 = s1.pop()
            arr.append(t1)

        if not s2.isEmpty():
            t2 = s2.pop()
            arr.append(t2)

        for item in arr:

            if s.isEmpty():
                s.push(item)

            else:
                if s.peek() > item:
                    s.push(item)
                else:
                    insert_sorted(s, item)

    print(s)


def insert_sorted(s, item):
    if s.isEmpty():
        s.push(item)
    elif s.peek() < item:
        c = s.pop()
        insert_sorted(s, item)
        s.push(c)
    else:
        s.push(item)


s1 = Stack()

s1.push(9)
s1.push(4)
s1.push(2)
s1.push(1)

s2 = Stack()

s2.push(8)
s2.push(17)
s2.push(3)
s2.push(10)

merge_stacks(s1, s2)
