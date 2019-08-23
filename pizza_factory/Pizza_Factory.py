from pizza_factory import Farmhouse_Pizza


class PizzaFactory():

    def __init__(self):
        self.toppings = ['A', 2, 5]

    def createPizza(self, choice):

        if choice == 1:
            return Farmhouse_Pizza(self.toppings)
        elif choice == 2:
            return None
        else:
            return None
