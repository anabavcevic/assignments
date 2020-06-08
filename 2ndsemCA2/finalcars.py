from car import Car, ElectricCar


def parseCommonAttributes(new_car, data):
        new_car.setColour(data.colour)
        new_car.setMake(data.make)
        # Mileage is not loaded from the inventory data.
        # new_car.setMileage(data.mileage)

class RentedItemMixin(object):
    """Simple class only tracking the renting status."""

    __rented = None

    def __init__(self):
        __rented = False

    def getRented(self):
        return self.__rented and True or False

    def setRented(self, rented):
        self.__rented = rented and True or False

    def rentOut(self):
        self.setRented(True)

    def returned(self):
        self.setRented(False)


class ImpElectricCar(ElectricCar, RentedItemMixin):
    """Improved electric car to support handy data-loading code."""

    def __init__(self):
        ElectricCar.__init__(self)
        RentedItemMixin.__init__(self)
    
    def loadData(self, data):
        """Set field values from the named tuple instance values."""
        # Add all of the specific attributes.
        self.setNumberFuelCells(int(data.num_cells))
        # Add all of the shared attributes.
        parseCommonAttributes(self, data)
        

class ICECar(Car, RentedItemMixin):
    """ICECar is common class for all internal-combustion-engine cars."""

    __fuel_type = None
    __number_cylinders = None

    def __init__(self):
        Car.__init__(self)
        RentedItemMixin.__init__(self)

    def loadData(self, data):
        """Set field values from the named tuple instance values."""
        # Add all of the specific attributes.
        self.setFuelType(data.fuel_type)
        self.setNumberCylinders(data.num_cylinders)
        # Add all of the shared attributes.
        parseCommonAttributes(self, data)

    def getFuelType(self):
        return self.__fuel_type

    def setFuelType(self, fuel_type):
        self.__fuel_type = fuel_type

    def getNumberCylinders(self):
        return int(self.__numberCylinders)

    def setNumberCylinders(self, value):
        self.__numberCylinders = int(value)


class HybridCar(ICECar, ImpElectricCar):
    """HybridCar class shares properties of both ICE and electric cars."""

    def __init(self):
        ICECar.__init__(self)
        ElectricCar.__init__(self)

    def loadData(self, data):
        """Take data data from the tuple and return an instance of HybridCar class."""
        ICECar.loadData(self, data)
        ImpElectricCar.loadData(self, data)
