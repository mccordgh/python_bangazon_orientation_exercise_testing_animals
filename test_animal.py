import unittest
from animals import *

class TestAnimalAndDog(unittest.TestCase):

	@classmethod  
	def setUpClass(cls):
	   	cls.animal = Animal()
	   	cls.animal.legs = 2
	   	cls.dog = Dog(cls.animal)
	   	cls.dog.legs = 4

	def test_AnimalMustHaveNameProperty(self):
		random_animal = Animal("Bilbo")
		self.assertEqual(random_animal.name, "Bilbo")

	def test_AnimalMustHaveSpeciesProperty(self):
		random_animal = Animal("Bilbo", "Chihuahua")
		self.assertEqual(random_animal.species, "Chihuahua")

	def test_InvokingWalkMethodSetsCorrectSpeedOnAnimalAndDog(self):
		animal_start_speed = self.animal.speed
		dog_start_speed = self.dog.speed
		self.animal.walk()
		self.dog.walk()
		self.assertEqual(self.animal.speed, animal_start_speed + (0.1 * self.animal.legs))
		self.assertEqual(self.dog.speed, dog_start_speed + (0.2 * self.dog.legs))

	def test_animalIsAnInstanceOfAnimal(self):
		self.assertIsInstance(self.animal, Animal)

	def test_dogIsAnInstanceOfDog(self):
		self.assertIsInstance(self.dog, Dog)


if __name__ == '__main__':
	unittest.main()



