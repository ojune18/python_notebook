from stack import Stack


class Node:

    def __init__(self, data, ind, left=0, right=0):
        self.data = data
        self.ind = ind
        self.left = left
        self.right = right

    def mutiplier(self):
        return self.left * self.right

    def __repr__(self):
        return "Data:: {} , Index {}, Left {}, Right {}\n".format(self.data, self.ind, self.left, self.right)


def main(arr):
    s = Stack()

    l = len(arr) - 1

    m = 0

    for item in range(len(arr) - 1, -1, -1):
        if item == l:
            s.push(Node(arr[item], item))

        elif arr[item] > s.peek().data:
            a = []
            n = Node(arr[item], item)
            while not s.isEmpty():
                elem = s.pop()
                a.append(elem)
                if arr[item] > elem.data:
                    if item+1 > elem.left:
                        elem.left = item + 1
                        m = max(m, elem.left * elem.right)
                elif arr[item] < elem.data:
                    n.right = elem.ind + 1
                    break
            while len(a) > 0:
                s.push(a.pop())

            s.push(n)

        elif arr[item] < s.peek().data:
            s.push(Node(arr[item], item, 0, s.peek().ind + 1))
        else:
            s.push(Node(arr[item],item))

    print(s,m)


main([1, 1, 1, 1, 0, 1, 1, 1, 1, 1])
