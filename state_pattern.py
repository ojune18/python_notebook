class Motion:

    def __init__(self):
        self.motion = 'Initial'
        pass

    def stop(self):
        return Stop()

    def change_motion(self):
        return Walk()


class Walk(Motion):

    def __init__(self):
        super().__init__()
        self.motion = 'Walking'

    def change_motion(self):
        return Run()


class Run(Motion):

    def __init__(self):
        super().__init__()
        self.motion = 'Run'

    def change_motion(self):
        return Walk()


class Stop(Motion):
    def __init__(self):
        super().__init__()
        self.motion = 'Stop'

    def change_motion(self):
        return Walk()


class Toy():

    def __init__(self):
        self.motion = Motion()

    def motion_transition(self):
        self.motion = self.motion.change_motion()

    def stop(self):
        self.motion = self.motion.stop()


t = Toy()


def run():
    flag = True
    while flag:
        yes_no = input(
            f'The current motion state is {t.motion.motion}. Do you wish to change the state? Type "yes" else any key\n')
        if yes_no == 'yes':
            t.motion_transition()
        else:
            t.stop()
            print(f"Motion stopped")
            final_input = input("Do you wish to restart the things? Press 1 otherwise anykey\n")
            if final_input == '1':
                t.motion_transition()
            else:
                return


run()
