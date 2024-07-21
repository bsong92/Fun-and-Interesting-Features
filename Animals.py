class Dog:
    scientific_name = "Canis lupus familiaris"
    
    def __init__(self, name):
        self.name = name
        self.woofs = 0

    def speak(self):
        print("Woof!")
    
    def eat(self, food):
        if food == 'biscuit':
            print("Yummy!")
        else:
            print("That's not food!")
        
    #def learn_name(self, name):
     #   self.name = name

    def hear(self, words):
        if self.name in words:
            self.speak()

    def count(self):
        self.woofs += 1
        for bark in range(self.woofs):
            self.speak()

        
class Cat:
    def __init__(self):
        self.mood = "neutral"
    
    def speak(self):
        if self.mood == "neutral":
            print("Meow!")
        elif self.mood == "happy":
            print("Purrr")
        elif self.mood == "angry":
            print("Hiss!")

class Husky(Dog):
    Origin = "Italy"

    def speak(self):
        print("Heyheyhey")




# When calling the eat method, you only need to pass it
# one argument, even though there are two parameters:
# spot.eat("biscuit")
# spot.eat("chair")


