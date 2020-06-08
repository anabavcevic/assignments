import csv
import dealership
import os

from collections import namedtuple
from finalcars import ICECar, HybridCar, ImpElectricCar


# Utility dictionary mapping strings of car classes to implementation
# classes. This saves me from verbose if ... elif ... elif ... elif structures.
_NAME_CLASS_MAP = {
    'ICECar': ICECar,
    'ElectricCar': ImpElectricCar,
    'HybridCar': HybridCar,
}


# Utility dictionary mapping internal implementation classes to strings.
# This is a reverse of _NAME_CLASS_MAP and serves the same purpose: avoiding
# verbose if ... elif statements.
_CLASS_NAME_MAP = {
    ICECar: 'ICECar',
    ImpElectricCar: 'ElectricCar',
    HybridCar: 'HybridCar',
}


# StorageClass is used internally to store the path to the source CSV file
# along with the loaded data. The path may come in handy in the future
# if we'll want to store changes to the inventory, as opposed to changes
# in rental statuses, which are stored separately.
StorageClass = namedtuple("StorageClass", ['path', 'cars'])


def loadData(data_class, data_path):
    """Open CSV file and load the data contained therein using the specified data class.

    Args:
        data_class: Class used to instantiate internal representation for
          each of the cars.
        data_path: A path to the input CSV file with car data.

    Returns:
        A map of car instances initialized using data from the CSV file. Map key
        is identifier (must be unique per file) and value is the instance created
        using the data_class class.
    """
    ret = {}  # At return this will contain car data.

    with open(data_path) as data:  # Open the file for reading.
        reader = csv.reader(data, delimiter=',')  # Create CSV reader.

        # Read first row which constains field names. If the row doesn't
        # exist, a StopIteration will be raised. In this case print
        # a message with the data path (may aid in debugging the issue)
        # and return an empty map.
        try:
            CarRowData = namedtuple("CarRowData", next(reader))
        except StopIteration:
            print('No data found in {name}'.format(name=data_path))
            return ret

        # For each next row returned from the reader ...
        for row in map(CarRowData._make, reader):
            # ... create a new instance using data_class and load
            # the row data using the loadData method.
            new_car = data_class()
            new_car.loadData(row)
            ret[row.id] = new_car

    return ret  # Return loaded car data.


class Dealership(dealership.Dealership):
    """Dealership class supported by the backind database in CSV files.

    Args:
      data_path: A string specifying the path to the dealership database.
    """

    # Declare fields for visibility. It is easier to name all fields
    # separately and explicitly instead of trying to identify them in __init__()
    # or other methods.
    __data_path = None  
    __inventory_map = None

    def __init__(self, data_path):
        dealership.Dealership.__init__(self)
        self.__data_path = data_path  # Set the current database path.
        self.__inventory_map = {}  # Ensure that inventory is not an invalid object.
        self.create_current_stock()  # Load the data using the member variable.

    def create_current_stock(self):
        """Create current stock creates or loads the current stock of cars."""

        # Database consists of multiple files. inventory.csv maps inventory
        # storage to Python car class. This loads all of the inventory data
        # from all of the files.
        with open(os.path.join(self.__data_path, 'inventory.csv')) as inv:  # Open 'inventory.csv' for reading.
            reader = csv.reader(inv, delimiter=',')  # Create CSV reader.

            # Read the first row with field names and use the names to create a new namedtuple class.
            # Namedtuple class makes for more readable code and flexibility, because I can use field
            # names directly instead of using indexes. E.g. instead of row[2], I can use row.car_class syntax
            # and if column ordering changes, the code doesn't have to change.
            InvRowData = namedtuple("InvRowData", next(reader))

            # Read all remaining rows using the InvRowData namedtuple class.
            for row in map(InvRowData._make, reader):
                # "storage" column (row.storage) specifies the name of CSV file with car data.
                data_path = os.path.join(self.__data_path, row.storage)
                # Use _NAME_CLASS_MAP to map car_class string to an internal class.
                data_class = _NAME_CLASS_MAP[row.car_class]
                # Store the data path and loaded car data together in the instance inventory.
                self.__inventory_map[data_class] = StorageClass(
                    path=data_path,
                    cars=loadData(data_class, data_path),  # Use loadData to load car data.
                )

        # Status data changes fast (renting out, recording mileage), inventory data
        # changes slower (car make, model, colour, ...). This is why status is stored
        # separately.
        self.load_statuses()


    def get_cars_petrol(self):
        # Use list comprehenstion to return only those instances of ICECar that
        # use 'petrol' as the fuel type.
        return [
            car for car in self.__inventory_map[ICECar].cars.values()
            if car.getFuelType() == 'petrol']

    def get_cars_diesel(self):
        # Use list comprehenstion to return only those instances of ICECar that
        # use 'diesel' as the fuel type.
        return [
            car for car in self.__inventory_map[ICECar].cars.values()
            if car.getFuelType() == 'diesel']

    def get_cars_electric(self):
        return self.__inventory_map[ImpElectricCar].cars.values()

    def get_cars_hybrid(self):
        return self.__inventory_map[HybridCar].cars.values()

    def stock_count(self):
        # All of the print statements use list comprehension to only count
        # cars that are not currently rented.

        print('Petrol cars in stock: {num}'.format(
            num=len([
                car for car in self.get_cars_petrol()
                if not car.getRented()])))

        print('Electric cars in stock: {num}'.format(
            num=len([
                car for car in self.get_cars_electric()
                if not car.getRented()])))

        print('Diesel cars in stock {num}'.format(
            num=len([
                car for car in self.get_cars_diesel()
                if not car.getRented()])))

        print('Hybrid cars in stock: {num}'.format(
            num=len([
                car for car in self.get_cars_hybrid()
                if not car.getRented()])))

    def process_rental(self):
        answer = input('Would you like to rent a car? y/n\n')
        if answer != 'y':
            return

        while True:
            answer = input('What type would you like?\n p: petrol\n d: diesel\n e: electric\n h: hybrid\n a: abort\n')
            if answer == 'a':
                return
            if answer in ['p', 'd', 'e', 'h']:
                break

        # Retrieve the correct list of cars, depending on the car type.
        if answer == 'p':
            cars = self.get_cars_petrol()
        elif answer == 'd':
            cars = self.get_cars_diesel()
        elif answer == 'e':
            cars = self.get_cars_electric()
        elif answer == 'h':
            cars = self.get_cars_hybrid()
        
        # Available cars are only those cars that are not currently rented.
        available = [car for car in cars if not car.getRented()]

        while True:
            answer = input('How many cars would you like? Maximum {num}, "a" to abort.\n'.format(num=len(available)))
            if answer == 'a':
                return
            amount = int(answer)
            if str(amount) != answer:
                print('You have entered an invalid number')
                continue
            if amount > 0 and amount <= len(available):
                break
            print('Enter "a" to abort or a positive number of cars you wish to rent, up to a maximum of {num}.'.format(
                num=len(available)
            ))

        self.rent(available, amount)
        self.stock_count()
        self.save_statuses()

    def rent(self, car_list, amount):
        # car_list contains only available cars, so it's sufficient to take first "amount"
        # cars and call rentOut() method on them to mark them rented out.
        for i in range(amount):
            car_list[i].rentOut()

    def load_statuses(self):
        with open(os.path.join(self.__data_path, 'status.csv')) as status:
            reader = csv.reader(status, delimiter=',')
            StatRowData = namedtuple("StatRowData", next(reader))
            for row in map(StatRowData._make, reader):
                car = self.__inventory_map[_NAME_CLASS_MAP[row.car_class]].cars[row.id]
                car.setMileage(row.mileage)
                car.setRented(row.rented and True or False)

    def all_cars(self, row_class):
        for car_class, cars in [(_CLASS_NAME_MAP[it[0]], it[1].cars) for it in self.__inventory_map.items()]:
            for id, car in cars.items():
                yield row_class(
                    car_class=car_class,
                    id=id,
                    mileage=car.getMileage(),
                    rented=car.getRented()
                )

    def save_statuses(self):
        StatRowData = namedtuple("StatRowData", ['car_class', 'id', 'mileage', 'rented'])
        with open(os.path.join(self.__data_path, 'status.csv'), 'w') as status:
            writer = csv.writer(status, delimiter=',')
            writer.writerow(StatRowData._fields)

            for row in self.all_cars(StatRowData):
                if row.mileage or row.rented:
                    # Only record cars that have non-zero mileage or are rented.
                    writer.writerow(row)