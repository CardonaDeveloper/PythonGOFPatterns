class Pizza:
    def __init__(self):
        self.base = None
        self.toppings = []
        self.diameter = None
        self.dough_color = None
        self.cheese_color = None
        self.number_of_slices = None

    def __str__(self):
        return (
            f"Base: {self.base}, "
            f"Diameter: {self.diameter}, "
            f"Dough Color: {self.dough_color}, "
            f"Cheese Color: {self.cheese_color}, "
            f"Slices: {self.number_of_slices}, "
            f"Toppings: {self.toppings}"
        )
