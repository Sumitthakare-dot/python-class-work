class Animal:
    def speak(self):
        print("I make a sound!")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")


animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()