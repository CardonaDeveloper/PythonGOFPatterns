from  .pizza import Pizza


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_base(self, base: str) -> "PizzaBuilder":
        self.pizza.base = base
        return self

    def set_diameter(self, diameter: float) -> "PizzaBuilder":
        self.pizza.diameter = diameter
        return self

    def set_dough_color(self, color: str) -> "PizzaBuilder":
        self.pizza.dough_color = color
        return self

    def set_cheese_color(self, color: str) -> "PizzaBuilder":
        self.pizza.cheese_color = color
        return self

    def set_number_of_slices(self, slices: int) -> "PizzaBuilder":
        self.pizza.number_of_slices = slices
        return self

    def add_toppings(self, *toppings: str) -> "PizzaBuilder":
        self.pizza.toppings.extend(toppings)
        return self

    def build(self) -> Pizza:
        return self.pizza
