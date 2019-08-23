from linkedlist.Node import Node


class OrderedLinkedList:

    def __init__(self):
        self.head = None

    def add(self, node):
        if node:
            if not self.head:
                self.head = node
                return

            else:
                current = self.head

                if current.data > node.data:
                    node.next, self.head = self.head, node
                    return

                while current:
                    if current.next is not None:
                        if current.next.data > node.data:
                            node.next, current.next = current.next, node
                            return
                        current = current.next
                    else:
                        current.next = node
                        current = None



        return

    def traverse(self):

        current = self.head

        while current:
            print(current.data, end="\t")
            current = current.next

        return


l = OrderedLinkedList()

n = Node(56)

n1 = Node(21)

n2 = Node(78)
n3 = Node(89)

n4 = Node(19)

l.add(n)
l.add(n1)
l.add(n2)
l.add(n3)
l.add(n4)

l.traverse()