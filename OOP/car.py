class Car():
    def __init__(self,name,year,color,forsale):
        self.name = name
        self.year=year
        self.color=color
        self.forsale=forsale
    
    def drive(self):
        print(f"YOU DRIVE {self.name}")
    def stop(self):
        print(f"YOU STOPPED {self.name} ")
    def describe(self):
        print(f"YOU DRIVE {self.color} {self.name} released in {self.year}")