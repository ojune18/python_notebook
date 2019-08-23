from stack import Stack

while True:
    string = input("Enter a string to reverse or \n'0' to quit from program\n")

    if string == '0':
        break

    s = Stack()
    for item in string:
        s.push(item)

    rev_str = ''

    while not s.isEmpty():
        rev_str += s.pop()

    print("Reversed String is => ", rev_str)
