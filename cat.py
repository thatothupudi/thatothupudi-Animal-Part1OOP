from animal import Animal

class Cat(Animal):

    def __init__(self,petname,sound):
        super().__init__(petname,sound)

    def food(self):
        print(self.name + " eats")

    def sounds(self):
        print(self.name + "meows")

cat1 = Cat("Stormy ","")
cat1.food()
cat1.sounds()