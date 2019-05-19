class SimpleMotion:
    def __init__(self):
        self.behaviour = 'simple'

    def execute(self):
        print(self.behaviour)


class TransitionMotion:
    def __init__(self):
        self._type = 'auto'

    def execute(self):
        print(self._type)


class ControlMotion:
    def __init__(self):
        self._control = 'remote'

    def execute(self):
        print(self._control)

class MoveToy:



    def __init__(self,motion_type):
        self._toy_move_type = motion_type

    def move(self):
        self._toy_move_type.execute()


t = TransitionMotion()
t1 = ControlMotion()
t2 = SimpleMotion()

toy = MoveToy(t)
toy.move()

toy = MoveToy(t1)
toy.move()

toy = MoveToy(t2)
toy.move()
