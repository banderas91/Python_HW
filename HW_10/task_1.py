class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def info(self):
        print(f"{self.name} является {self.species}.")

class Fish(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def swim(self):
        print(f"{self.name} плывет.")

class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def fly(self):
        print(f"{self.name} летит.")

class Mammal(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def run(self):
        print(f"{self.name} бежит.")

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name, species):
        if animal_type == "Fish":
            return Fish(name, species)
        elif animal_type == "Bird":
            return Bird(name, species)
        elif animal_type == "Mammal":
            return Mammal(name, species)
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")


fish = AnimalFactory.create_animal("Fish", "Nemo", "рыба клоун")
fish.info()  
fish.swim()  