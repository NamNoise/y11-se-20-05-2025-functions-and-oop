class Pet():
    def __init__ (self, weight, number_legs, colour, name):
        self.number_legs = number_legs
        self.colour = colour
        self.weight = weight
        self.name = name
        self.food_eaten = 0

    def is_hungry(self):
        if self.food_eaten < 10:
            print (self.name + " is hungry. Please feed him")
        else:
            print (self.name + " is not hungry")

        return self.food_eaten < 10

    def feed(self, food_amount):
        self.food_eaten += 10

class Dog(Pet):
    def __init__ (self, weight, colour, name):
        super().__init__ (weight, 4, colour, name)

    def make_noise(self):
        print (f"{self.name} goes 'Woof!!'")


my_dog = Dog(10, "brown", "Wookie")
my_dog.make_noise()
my_dog.is_hungry()

my_dog.feed(10)
my_dog.is_hungry()

# TODOs
# Create a Cat Class (that is a Pet) 
# - The Cat is still hungry unless it's eaten 100 food
# - The Cat makes a noise 'Meow!!'
# Work out how to make the hungry_amount a value instead of copying the code
