from builder_pattern.pizza_builder import PizzaBuilder


class ClassicPizzaBuilder(PizzaBuilder):
    def set_base(self):
        self.pizza.base = "Clasica"
        return self

    def set_diameter(self):
        self.pizza.diameter = 12
        return self

    def set_dough_color(self):
        self.pizza.dough_color = "Blanco"
        return self

    def set_cheese_color(self):
        self.pizza.cheese_color = "Amarillo"
        return self

    def set_number_of_slices(self):
        self.pizza.number_of_slices = 8
        return self

    def add_toppings(self):
        self.pizza.toppings.extend(["Salsa de tomate", "Mozzarella", "Pepperoni"])
        return self
