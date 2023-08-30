"""
This code defines an Animal class with methods to access and change an animal's species, 
demonstrating how protected attributes and methods can be used to interact with them in a controlled manner
"""
class Animal:
    def __init__(self, nombre: str, especie: str):
        self.nombre = nombre
        self._especie = especie  # The underscore at the beginning indicates that it's a protected variable

    def get_especie(self) -> str:
        return self._especie

    def change_especie(self, nueva_especie: str) -> None:
        self._especie = nueva_especie

if __name__ == "__main__":   
    animal = Animal("Chewie", "Dog")
    print("Original species:", animal.get_especie())

    animal.change_especie("Cat")
    print("New animal species:", animal.get_especie())  