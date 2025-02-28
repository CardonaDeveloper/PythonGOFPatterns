from singleton_pattern.generic_example.singleton import Singleton
from singleton_pattern.logger_example.logger import Logger
from singleton_pattern.anotation_example.anotation_example import SingletonLogger


print("\n----------------------------------")
print("\n----------------------------------")
print("\n----Singleton Pattern Generic-----")
print("\n----------------------------------")
print("\n----------------------------------")


singleton1 = Singleton(value="Primera instancia")
singleton2 = Singleton(value="Segunda instancia")

# Verificamos si son la misma instancia
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


print("\n-----------------------------------")
print("\n-----------------------------------")
print("\nSingleton Pattern Logger Annotation")
print("\n-----------------------------------")
print("\n-----------------------------------")

annotation_logger1 = SingletonLogger()
annotation_logger2 = SingletonLogger()

annotation_logger1.log("Este es un mensaje de prueba logger.")
annotation_logger2.log("Este es otro mensaje para el logger.")

print(annotation_logger1 is annotation_logger2)  
print(f"Mostrando la referencia del objeto 1 --> {annotation_logger1}")
print(f"Mostrando la referencia del objeto 2 --> {annotation_logger2}")