from stack import Stack


class ReverseStack(Stack):

    def reverse(self, item=None):

        if not self.isEmpty():
            c = self.pop()
            self.reverse(c)
            self._insertAtBottom(c)

        return self._item

    def _insertAtBottom(self, item):

        if self.isEmpty():
            self.push(item)
        else:
            c = self.pop()
            self._insertAtBottom(item)
            self.push(c)


s = ReverseStack()

s.push(3)
s.push(4)
s.push(5)
s.push(6)

print(s.reverse())
