class Animal:
#Initializing the variables 
    def __init__(self,petname,sound,eats):
        self.name = petname
        self.sound = sound
        self.eats = eats

    def eat(self):
        print(self.eats)
        return "{0}".format(self.eats)


    def sounds(self):
        print(self.sound)
        return "{0}".format(self.sound)


    
dog = Animal("Dog","barks", "food")

dog.eat()
dog.sounds()

cat = Animal("Cat","meows", "food")

cat.eat()
cat.sounds()
