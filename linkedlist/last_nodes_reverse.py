from linkedlist.Node import Node
from linkedlist import LinkedList
from stack import Stack


class ModifyPrint(LinkedList):

    def reverse_print(self, k=0):

        if k > 0:
            s = Stack()
            current = self.head

            while current:
                s.push(current.data)
                current = current.next

            while k > 0:
                k -= 1
                print(s.pop())

        return


l = ModifyPrint()
l.add(Node(2))
l.add(Node(21))
l.add(Node(32))
l.add(Node(3))
l.add(Node(8))
l.add(Node(90))

l.reverse_print(3)
