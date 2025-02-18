from builder_pattern.classic_pizza_builder import ClassicPizzaBuilder
from builder_pattern.director import PizzaDirector
from builder_pattern.vegan_pizza_builder import VeganPizzaBuilder


classic_builder = ClassicPizzaBuilder()
director = PizzaDirector(classic_builder)
classic_pizza = director.construct_pizza()
print("Classic Pizza:")
print(classic_pizza)


vegan_builder = VeganPizzaBuilder()
director = PizzaDirector(vegan_builder)
vegan_pizza = director.construct_pizza()
print("\n Vegan Pizza:")
print(vegan_pizza)
