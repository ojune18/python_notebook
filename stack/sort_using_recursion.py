from stack import Stack


class SortedStack(Stack):

    def sort_stack(self):

        if not self.isEmpty():
            temp = self.pop()

            self.sort_stack()

            self._insert_sorted(temp)

        return self._item

    def _insert_sorted(self, item):

        if self.isEmpty():
            self.push(item)

        else:

            if self.peek() > item:
                t = self.pop()
                self._insert_sorted(item)
                self.push(t)
            else:
                self.push(item)


s = SortedStack()
s.push(30)
s.push(-5)
s.push(18)
s.push(14)
s.push(-3)

print(s.sort_stack())
