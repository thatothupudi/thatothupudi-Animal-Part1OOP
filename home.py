from animal import Animal
from dog import Dog
from cat import Cat

class Home:
    
    def __init__(self, pets = []):
        self.pets = pets

    def adopt_pet(self,pet):
        for each_pet in self.pets:
            if each_pet == pet:
                raise Exception("You cannot adopt the same pet twice")
        self.pets.append(pet)

    def sounds(self):
        return dog_1.food()

if __name__ == "__main__":
    
    home = Home()
    
    dog_1 = Dog("Rax","barks")
    cat_1 = Cat("Stormy","meows")
    
    home.adopt_pet(dog_1)
    home.adopt_pet(cat_1)
    
    print("\nThese are pets you can adopt: ")
    print(home.pets[0].name)
    print(home.pets[1].name)