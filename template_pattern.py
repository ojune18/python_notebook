class Toy:

    def __init__(self, name):
        self.name = name

    def play(self):
        print('play with toy')


class RemoteCar(Toy):

    def __init__(self, name):
        super().__init__(name)

    def controls(self):
        print(f'{self.name} is a remote controlled car')


class PullAndReleaseCar(Toy):

    def __init__(self, name):
        super().__init__(name)

    def controls(self):
        print(f'{self.name} has manual controls')
