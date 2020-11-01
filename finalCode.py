# Copy this code into your own repl. Click the navigation bar in the top left corner and go to My Repl.
# Click the New Repl on the left, create the repl, and paste the code. Or put into another IDE

# Today we will learn about Python Classes and Objects

# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# To create a class, we use the keyword class. Example: class nameOfClass
class dollarBill:
    value = 1

# Now lets create an object by using the class.
p1 = dollarBill()           # p1 now takes on the property value = 1
print(p1.value)             # When we print p1's value, it will be 1

# The last example was a class and object in the simplest form. The _init_() function is where it get interesting.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary
# to do when the object is being created:

class Person:                          # This creates the class
    def __init__(self, name,age):        # Consider this the blueprint
        self.name = name               # Assigns the name argument to the name variable
        self.age = age                 # Assigns the age argument to the age variable
    def myfunc(self):
        print("Hello my name is " + self.name + ". I am " + str(self.age) + " years old.")

h1 = Person("Harold", 27)       # We create an object of the person class with the name Harold and age 27 and assign it to h1
john = Person("John", 78)
ava = Person("Ava", 47)

print(ava.age)
print(h1.name)

# Classes can contain methods.
# Lets add one to the Person class. Add the one below
"""
def myfunc(self):
    print("Hello my name is " + self.name ". I am " + self.age + " years old.")
"""
# Now lets call it

john.myfunc()
h1.myfunc()

# Notice the first parameter of the Person _init_. The self parameter is a little confusing. Here is what you should know
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

# We can modify object properties. Imagine if Ava had a birthday and is now 48.
ava.age = 48

# We can delete the age property if we wanted with the keyword del
del ava.age

# We can delete the object as a whole too
del ava

# Lets make a class that is a blueprint for a car factory. First, what are some characteristics of a car?
# What value type (string, int, double, boolean) is the characteristic. For instance, miles would be an int.
# List at least 3 characteristics and the value type below.

# Model of Car. String
# Miles on Car. Int
# Price of Car. Double

# Now lets make the class Car. Create the _init_() functions with 4 parameters, 3 the car's characteristics, and don't forget self.
# Then create a function called description(self) which prints a description of the car using the objects properties.
# Now create an object of the Car class!

class Car:
    def __init__(self, model, miles, price):
        self.model = model
        self.miles = miles
        self.price = price

    def description(self):
        print("The " + self.model + " with " + str(self.miles) + " miles, will cost $" + str(self.price) + ".")

car1 = Car("2018 Mazda CX 5 Touring", 32064, 18493.99)

car2 = Car("2015 Tesla Model S 70", 36449, 41400.87)

car3 = Car("2014 Chevrolet Malibu LS", 102246, 9351.22)

print(car1)            # Prints out the location of the object. Not useful to client
car1.description()     # Prints useful information
car2.description()
car3.description()
