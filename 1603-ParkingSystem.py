class ParkingSystem:

    def __init__(self, big, medium, small):
        self.spaces = [big,medium,small]

    def addCar(self, carType) :
        if self.spaces[carType-1] > 0:
            self.spaces[carType-1] -=1
            return True
        return False
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)