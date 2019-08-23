from abc import ABC, abstractmethod


class Pizza():

    def __init__(self, factory):
        self.ingredients_factory = factory


    @abstractmethod
    def add_toppings(self,toppings):
        pass


