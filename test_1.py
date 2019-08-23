def air_travel_strategy():
    print('you are travelling using air mode')


def cab_travel_strategy():
    print('you are travelling using a cab')


def bus_travel_strategy():
    print('you are travelling using a bus')


def travel(strategy):
    strategy()


travel(air_travel_strategy)

travel(cab_travel_strategy)

print("\t\t\tSimple Factory")


class AirTravel:

    def __init__(self):
        self.mode = 'air'

    def travel(self):
        print(f'You have chosen to travel by {self.mode}')


class CabTravel:

    def __init__(self):
        self.mode = 'cab'

    def travel(self):
        print(f'You have chosen to travel by {self.mode}')


class BusTravel:

    def __init__(self):
        self.mode = 'bus'

    def travel(self):
        print(f'You have chosen to travel by {self.mode}')


def travel_factory(budget=100):
    if budget > 1000:
        return AirTravel()
    elif budget <= 1000 and budget > 500:
        return CabTravel()
    else:
        return BusTravel()


travel_factory(1000).travel()

travel_factory(4000).travel()

travel_factory(400).travel()

print(globals())

print("\t\t\tAdapter Pattern")


def travel(ticket):
    if ticket:
        print('Allowed to travel')
    else:
        print('not allwoed')

