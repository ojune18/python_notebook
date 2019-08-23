from linkedlist.Node import Node


class LinkedList():

    def __init__(self):
        self.head = None

    def add(self, node=None):

        if self.head is None:
            self.head = node

        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def traverse(self):
        l = []
        current = self.head
        while current:
            l.append(current.data)
            current = current.next

        return " ".join(map(str, l))
