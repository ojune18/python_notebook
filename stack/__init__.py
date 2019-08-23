class Stack:

    def __init__(self):
        self._item = []

    def push(self, item):
        self._item.append(item)

    def pop(self):
        return self._item.pop()

    def peek(self):
        return self._item[len(self._item) - 1]

    def size(self):
        return len(self._item)

    def isEmpty(self):
        return True if len(self._item) == 0 else False

    def __repr__(self):
        return " ".join(map(str, self._item))
