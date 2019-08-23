from stack import Stack

opening = {'}': '{', ']': '[', ')': '('}

while True:
    string = input("Enter Set of Parenthesis\n'0' to quit\n")

    if string == '0':
        break

    string = string.replace(" ","")

    s = Stack()

    res = True

    for item in string:
        if item in opening.keys() and not s.isEmpty():
            c = s.pop()
            if not c == opening[item]:
                res = False
                break
        elif item in opening.values():
            s.push(item)
        else:
            res = False
            break

    if res and s.isEmpty():
        print('Balanced Parenthesis')
    else:
        print('Non balanced Parenthesis')
