from stack import Stack


class OddStack(Stack):

    def remove_even_elems(self):

        if not self.isEmpty():
            c = self.pop()
            self.remove_even_elems()
            if c % 2 != 0:
                self.push(c)

        return self


o = OddStack()

o.push(2)
o.push(11)
o.push(12)
o.push(9)
o.push(1)
o.push(6)

print(o.remove_even_elems())

