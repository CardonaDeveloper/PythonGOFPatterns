from .pizza_builder import PizzaBuilder


class VeganPizzaBuilder(PizzaBuilder):
    def set_base(self):
        self.pizza.base = "Whole wheat crust"
        return self

    def set_diameter(self):
        self.pizza.diameter = 10
        return self

    def set_dough_color(self):
        self.pizza.dough_color = "Light brown"
        return self

    def set_cheese_color(self):
        self.pizza.cheese_color = "White (Vegan cheese)"
        return self

    def set_number_of_slices(self):
        self.pizza.number_of_slices = 6
        return self

    def add_toppings(self):
        self.pizza.toppings.extend(
            ["Tomato sauce", "Vegan cheese", "Mushrooms", "Olives", "Peppers"]
        )
        return self
