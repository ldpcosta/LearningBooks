### Animal is-a object

class Animal(object):
	pass

##  Dog is-a Animal

class Dog(Animal):

	def __init__(self, name):
		## Dog has-a name
		self.name = name

## Cat is-a Animal

class Cat(Animal):

	def __init__(self, name):
		## Cat has-a name
		self.name = name

## Person is-a Object
class Person(object):
	def __init__(self, name):
		## Person has-a name
		self.name = name

		## Person has-a pet
		self.pet = None

## Employee is-a person
class Employee(Person)
	def __init__ (self, name, salary):
		## Employee has the same name as the Person
		super(Employee, self).__init__(name)

		## Employee has-a salary
		self.salary = salary

## Fish is-a object

class Fish(object):
	pass

## Salmon is-a fish

class Salmon(Fish):
	pass

## Rover is-a Dog

rover = Dog("Rover")

## Satan is-a cat

satan = Cat("Satan")

## Mary is-a person

mary = Person("Mary")

## Mary has-a pet (satan)

mary.pet = satan

## Frank is a Employee

frank = Employee("Frank",120000)

## Flipper is a fish

flipper = Fish()

## Crouse is a Salmon

crouse = Salmon()

## Harry is a halibut

harry = Halibut()