from .pizza_builder import PizzaBuilder


class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def construct_pizza(self):
        return (
            self.builder.set_base()
            .set_diameter()
            .set_dough_color()
            .set_cheese_color()
            .set_number_of_slices()
            .add_toppings()
            .build()
        )
