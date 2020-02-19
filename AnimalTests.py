import unittest

from animal import Animal
from cat import Cat
from dog import Dog

class AnimalTests(unittest.TestCase):
    
    def setUp(self):
        print('setUp')
        self.dog1 = Animal("Dog","barks", "food")
        self.cat1 = Animal("Cat","meows", "food")
    
    def testDogSound(self):
        print("testDogSound")
        self.assertEqual(self.dog1.sound, 'barks')
    
    def testDogEats(self):
        print("testDogEats")
        self.assertEqual(self.dog1.eats, 'food')
    
    def testCatSound(self):
        print("testCatSound")
        self.assertEqual(self.cat1.sound, 'meows')
    
    def testCatEats(self):
        print("testCatEats")
        self.assertEqual(self.cat1.eats, 'food')
    
    
    # def testDog(self):
        
    #     if str('food'.casefold and 'FOOD'.casefold and 'Food'.casefold) in str(self.eats):
    #         print('That can certainly be found here.')
    #         self.sleep(2)
    #         assert f"If you know where to look..."
        
            
if  __name__ == "__main__":
    unittest.main()