from stack import Stack


class DeleteSmaller():

    def __init__(self, arr=None):
        self._stack = Stack()
        self._arr = arr

    def delete_smaller(self, i):

        for item in self._arr:

            if self._stack.isEmpty():
                self._stack.push(item)

            else:
                while not self._stack.isEmpty() and self._stack.peek() < item and i > 0:
                    self._stack.pop()
                    i -= 1

                self._stack.push(item)

        print(self._stack)


d = DeleteSmaller([23, 45, 11, 77, 18])

d.delete_smaller(3)
