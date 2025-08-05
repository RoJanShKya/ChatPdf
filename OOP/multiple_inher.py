class prey:
    def __init__(self,name):
        self.name=name
    def flee(self):
        print(f"{self.name} flees")
class predator:
    def hunt(self):
        print(f"{self.name} hunts")
class rabbit(prey):
    pass
class Hawk(predator):
    pass
class fish(prey,predator):
    pass
Fish = fish("rohumacha")
Fish.flee()
Fish.hunt()