from stack import Stack


class MinStack(Stack):

    def __init__(self):
        super()
        self._min = -1

    def push(self, item):
        if self._min > -1:
            self._min = 0
            self._item.append(item)
        else:
            if item < self._item[self._min]:
                self._item.append(item)
                self._min = len(self._item) - 1
            else:
                self._item.append(item)

    def pop(self):

        if self._min == len(self._item) - 1:
            # Find new min index
            pass
        else:
            self._item.pop()

    def get_min(self):
        return self._item[self._min] if self._min > -1 else 'Empty stack'


