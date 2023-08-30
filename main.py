"""
This code defines an Animal class with methods to access and change an animal's species, 
demonstrating how protected attributes and methods can be used to interact with them in a controlled manner
"""
class Animal:
    """
    This class represents an animal with a name and species
    """
    def __init__(self, nombre: str, especie: str):
        """
        Initialize an Animal object with a name and species

        param nombre: The name of the animal
        param especie: The species to which the animal belongs
        """
        self.nombre = nombre
        self._especie = especie  # The underscore at the beginning indicates that it's a protected variable

    def get_especie(self) -> str:
        """
        Gets the species of the animal
        return: The species of the animal
        """
        return self._especie

    def change_especie(self, nueva_especie: str) -> None:
        """
        Changes the species of the animal to a new species

        param nueva_especie: The new species of the animal
        """
        self._especie = nueva_especie

if __name__ == "__main__":   
    animal = Animal("Chewie", "Dog")

    print("Original species:", animal.get_especie())

    animal.change_especie("Cat")
    print("New animal species:", animal.get_especie())  


