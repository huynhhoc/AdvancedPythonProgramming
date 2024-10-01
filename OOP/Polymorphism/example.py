class Dog:
    def sound(self):
        return "Woof"


class Cat:
    def sound(self):
        return "Meow"


def make_sound(animal):
    return animal.sound()


# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

# Polymorphic function call
print(make_sound(dog))  # Outputs: Woof
print(make_sound(cat))  # Outputs: Meow