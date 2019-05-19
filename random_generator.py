import random

arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z', ' ']

p = 'methink its a weasel'
n = 100000
best = 0
start = 0
match = ''
while n > 0:
    start = 0
    i = len(p)
    s = ''
    while i > 0:
        i -= 1
        s += arr[random.randrange(27)]
    n -= 1

    for item in range(len(s)):
        if s[item] == p[item]:
            start += 1

    if start > best:
        print("Best => ", best, "\tString =>\t", s)
        match = s
        best = start

print("Best => ", best, "\tString =>\t", s)
