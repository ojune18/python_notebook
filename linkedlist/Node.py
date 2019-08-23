class Node:

    def __init__(self, data, next=None):
        self._data = data
        self._next = next

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next
