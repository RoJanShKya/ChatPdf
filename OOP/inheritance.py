

class animal:
    def __init__ (self,name):
        self.name=name
        self.isalive= True
    
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
                      

class Dog(animal):
    def speak(self):
        print(f"{self.name} is barking")
class Cat(animal):
    def speak(self):
        print(f"{self.name} is meowing")
cat=Cat("rohan")
print(cat.name)
cat.eat()
cat.sleep()
cat.speak()
print(cat.isalive)
