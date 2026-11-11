class Animal:     #creates the main class
    def __init__(self, name): #initializes this so that it will run kaagad when i create a child from it...
        self.name = name     #stores name

    def eat(self):
        print(self.name, "eats")

    def make_sound(self):
        print(self.name, "makes sounds")

class Lion(Animal):     # is the subclass of animal
    def __init__ (self, name):
        super().__init__(name)  #initializes the parent class

    def make_sound(self):      #overrides the make sound method of the main class
        print(self.name, "roars loudly!")

    def eat(self):     #overrides the eat method of the main class
        print(self.name, "eats fresh meat") 

class Elephant (Animal):      #also the subclass of animal
    def __init__ (self, name):
        super().__init__(name)  #initializes the parent class

    def make_sound(self): 
        print(self.name, "trumpets!")

    def eat(self):
        print(self.name, "eats grass and fruits")

class Monkey (Animal):
    def __init__ (self, name):
        super().__init__(name)  #initializes the parent class

    def make_sound(self):
        print(self.name, "chatters!")

    def eat (self):
        print(self.name, "eats bananas")

# the objects of the classes r created
    lion = Lion("Simba")
    elephant = Elephant("Dumbo")
    monkey = Monkey("George")

    lion.make_sound()
    lion.eat()
    print("-----")

    elephant.make_sound()
    elephant.eat()
    print("-----")

    monkey.make_sound()
    monkey.eat()
    print("-----")
