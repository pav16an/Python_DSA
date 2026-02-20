class vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
        
class car(vehicle):
    def __init__(self,brand,speed):
        super().__init__(brand,speed)
        
    def details(self):
        print(f"car brand is {self.brand} and it have {self.speed} speed")
        
        
car1 = car("ford",330)
car1.details()