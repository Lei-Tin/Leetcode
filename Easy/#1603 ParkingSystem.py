class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.small = small
        self.medium = medium
        self.big = big

    def addCar(self, carType: int) -> bool:
        match carType:
            case 3:
                if self.small == 0:
                    return False
                self.small -= 1
            case 2:
                if self.medium == 0:
                    return False
                self.medium -= 1
            case 1:
                if self.big == 0:
                    return False
                self.big -= 1

        return True

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
