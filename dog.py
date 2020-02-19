from animal import Animal

class Dog(Animal):

    def __init__(self,petname,sound,eats):
        super().__init__(petname,sound,eats)

    def eat(self):
        print(self.eats)
        return "{0}".format(self.eats)

    def sounds(self):
        print(self.sound)
        return "{0}".format(self.sound)

dog1 = Dog("Dog","barks ","food")
#dog1.eat()
dog1.sounds()