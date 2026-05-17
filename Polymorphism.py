#Same method name behaves differently.
class Dog:
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("Cat meows")
animals = [Dog(), Cat()]
for animal in animals:
    animal.sound()

o/p: Dog barks
     Cat meows
