from typing import *

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.capacity=[big,medium,small]
        self.inside=[0,0,0]

    def addCar(self, carType: int) -> bool:
        carType-=1
        if self.capacity[carType]==self.inside[carType]:
            return False
        self.inside[carType]+=1
        return True

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
