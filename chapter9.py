class Dog():
	"""A simple attempt to model a dog."""

	def __init__(self,name,age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)

print(my_dog.name.title())
print(type(my_dog.age))
my_dog.sit()
my_dog.roll_over()

class Car():
	"""A simple attempt to represent a car."""

	def __init__(self, make, model, year):
		"""Initialzie attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + " " + self.make + " " + self.model
		return long_name
	def read_odometer(self):
		"""Print a statement shwoing the car's mileage"""
		print("This car has " + str(self.odometer_reading) + " miles on it.")
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
		    self.odometer_reading = mileage
		else:
			print("You cannot roll back an odometer!")
	def increment_odometer(self, miles):
		self.odometer_reading += miles

my_new_car = Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.increment_odometer(20)
my_new_car.read_odometer()










