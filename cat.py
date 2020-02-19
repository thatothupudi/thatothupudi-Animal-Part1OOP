from animal import Animal

class Cat(Animal):

    def __init__(self,petname,sound,eats):
        super().__init__(petname,sound,eats)

    def eat(self):
        print(self.eats)
        return "{0}".format(self.eats)

    def sounds(self):
        print(self.sound)
        return "{0}".format(self.sound)

cat1 = Cat("Cat ","meows", "food")
#cat1.eat()
cat1.sounds()