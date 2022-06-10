#create a variable class
class Vehicle:
    def __init__ (self, _mileage, _maxspeed):
        self.mileage=_mileage
        self.maxspeed=_maxspeed   
audi=Vehicle(320,80)
mercedes=Vehicle(600,150)
print(audi.maxspeed,audi.mileage)
print(mercedes.maxspeed,mercedes.mileage)

