class PizzaStore:

    def __init__(self):
        self.choice = ''

    def order_pizza(self):
        print(
            "Enter pizza of your choice:\n\tOptions are:\n\t\t1.Peppy Paneer\n\t\t2. Margaritha\n\t\t3. Veg FarmHouse\n\t\t4. Country Special")

        pizza_choice = int(input("\n"));




pizzaStore = PizzaStore()

pizzaStore.order_pizza()
