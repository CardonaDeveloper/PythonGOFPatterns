from abc import ABC, abstractmethod

from .pizza import Pizza


class PizzaBuilder(ABC):
    def __init__(self):
        self.pizza = Pizza()

    @abstractmethod
    def set_base(self) -> "PizzaBuilder":
        pass

    @abstractmethod
    def set_diameter(self) -> "PizzaBuilder":
        pass

    @abstractmethod
    def set_dough_color(self) -> "PizzaBuilder":
        pass

    @abstractmethod
    def set_cheese_color(self) -> "PizzaBuilder":
        pass

    @abstractmethod
    def set_number_of_slices(self) -> "PizzaBuilder":
        pass

    @abstractmethod
    def add_toppings(self) -> "PizzaBuilder":
        pass

    def build(self):
        return self.pizza
