from stack import Stack

while True:

    string = input("Enter a infix equation\n'0' to quit\n")

    if string == '0':
        break

    str_list = []

    operators = ['-', '+', '*', '/']

    s = Stack()

    for item in string:
        if item == '(':
            s.push(item)
        elif item == ')':
            while True and not s.isEmpty():
                c = s.pop()

                if c == '(':
                    break
                else:
                    str_list.append(c)
        elif item in operators:
            while True and not s.isEmpty():
                if not s.isEmpty() and s.peek() in operators and operators.index(s.peek()) >= operators.index(item):
                    str_list.append(s.pop())
                else:
                    break
            s.push(item)
        else:
            str_list.append(item)

    while not s.isEmpty() :
        str_list.append(s.pop())

    print(str_list)
