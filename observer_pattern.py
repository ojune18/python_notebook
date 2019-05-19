#!../venv/bin/python
class DynamicPricing:

    def __init__(self):
        self._observers = []
        self._products_list = {}

    @property
    def product_list(self):
        return list(zip(self._products_list.keys(), self._products_list.keys()))

    def add_product(self, name, price=0):
        self._products_list.update({name: price})
        self._update_observer()

    def append_observer(self, observer):
        self._observers.append(observer)

    def _update_observer(self):
        for item in self._observers:
            item()


class Subscriber:

    def __init__(self, dynamicprice):
        self.prices = dynamicprice

    def __call__(self, *args, **kwargs):
        print(self.prices.product_list)


# d = DynamicPricing()
# s = Subscriber(d)
# d.append_observer(s)
#
# d.add_product('Shoes', 1100)
# d.add_product('Socks', 100)
# d.add_product('tie', 250)
# d.add_product('Shirt', 1100)
# d.add_product('Pants', 1500)

####################
"""Subscribing to different types of events"""


class SubscriptionException(Exception):
    pass


class Subscriber:

    def __init__(self, publisher):
        self._publisher = publisher
        self._event = ""

    def update(self, *args, **kwargs):
        print(args)

    def remove_subscription(self, event):
        if self._event == event:
            self._event = ""

    def subscribe(self, event):
        if self._event == "":
            self._publisher.append_event_subscriber(event,self)
            return
        raise SubscriptionException('Subscription queue is not Empty')


class Publisher:

    def __init__(self):

        self.event_queue = {}

    def append_event_subscriber(self, event, subscriber):
        self.event_queue[event] = self.event_queue.get(event,[])
        self.event_queue[event].append(subscriber)

    def dispatch(self, event, message):
        if event in self.event_queue.keys():
            for item in self.event_queue[event]:
                item.update(message)


p = Publisher()
s1 = Subscriber(p)
s2 = Subscriber(p)
s1.subscribe('lunch')
s2.subscribe('dinner')

p.dispatch('lunch', 'Its lunch time')
p.dispatch('dinner', 'Its dinner time')
