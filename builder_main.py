from builder_pattern.director_case.classic_pizza_builder import ClassicPizzaBuilder
from builder_pattern.director_case.director import PizzaDirector
from builder_pattern.director_case.vegan_pizza_builder import VeganPizzaBuilder
from builder_pattern.no_director.pizza_builder import PizzaBuilder
from singleton_pattern.generic_example.singleton import Singleton
from singleton_pattern.logger_example.logger import Logger

print("\n Creando pizza director:")

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


# No Director:

print("\n Creando pizza no director:")

pizza_no_director = (
    PizzaBuilder()
    .set_base("delgada")
    .set_diameter(30.0)
    .set_dough_color("dorada")
    .set_cheese_color("amarillo")
    .set_number_of_slices(8)
    .add_toppings("pepperoni", "champiñones", "aceitunas")
    .build()
)

print("\n Mostrando pizza no director:")
print(f"Pizza no director: --> {pizza_no_director}")



print("\n----------------------------------")
print("\n----------------------------------")
print("\n----Singleton Pattern Generic-----")
print("\n----------------------------------")
print("\n----------------------------------")


singleton1 = Singleton(value="Primera instancia")
singleton2 = Singleton(value="Segunda instancia")

## Verificamos si son la misma instancia
print(singleton1 is singleton2)  

# Imprimimos el valor
print(f"singleton1 -> {singleton1.get_value()}")  
print(f"singleton2 -> {singleton2.get_value()}")  

print("\n----------------------------------")
print("\n----------------------------------")
print("\n-----Singleton Pattern Logger-----")
print("\n----------------------------------")
print("\n----------------------------------")


logger1 = Logger()
logger2 = Logger()

logger1.log("Este es un mensaje de prueba.")
logger2.log("Otra entrada en el log.")



print(f"Ambos objetos apuntan a la misma instancia? R/{logger1 is logger2}")
print(f"Mostrando la referencia del objeto 1 --> {logger1}")
print(f"Mostrando la referencia del objeto 2 --> {logger2}")