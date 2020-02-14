from animal import Animal

class Dog(Animal):

    def __init__(self,petname,sound):
        super().__init__(petname,sound)

    def food(self):
        print(self.name + " eats")

    def sounds(self):
        print(self.sound + "barks")

dog1 = Dog("Rax","Dog ")
dog1.food()
dog1.sounds()