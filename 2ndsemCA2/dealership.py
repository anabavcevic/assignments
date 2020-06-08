
from car import Car, ElectricCar, PetrolCar

def dealership_init():
    red_car = Car()
    print('Colour ' + red_car.getColour())
    print('Mileage ' + str(red_car.getMileage()))
    print('Make ' + red_car.getMake())

    red_car.setMake('Ferrari')

    print('Make ' + red_car.getMake())

    print('Getting a paint job - the new colour is ' + red_car.paint('red'))

    print('Colour ' + red_car.getColour())

    print('Car moved' + str(red_car.move(15)) + 'kms')
    print('Mileage ' + str(red_car.getMileage()))

    print('Engine Size ' + red_car.engineSize)
    red_car.engineSize = '3.9'
    print('Engine Size ' + red_car.engineSize)


    car3 = ElectricCar()
    car3.setColour('white')
    car3.setMileage(500)
    car3.setNumberFuelCells(2)
    car3.move(20)
    print('Colour ' + car3.getColour())
    print('Number of fuel cells ' + str(car3.getNumberFuelCells()))


class Dealership(object):

    def __init__(self):
        self.electric_cars = []
        self.petrol_cars = []

    def create_current_stock(self):
        for i in range(20):
           self.electric_cars.append(ElectricCar())
        for i in range(10):
           self.petrol_cars.append(PetrolCar())

    def stock_count(self):
        print('petrol cars in stock ' + str(len(self.petrol_cars)))
        print('electric cars in stock ' + str(len(self.electric_cars)))

    def rent(self, car_list, amount):
        if len(car_list) < amount:
            print('Not enough cars in stock')
            return
        total = 0
        while total < amount:
           car_list.pop()
           total = total + 1

    def process_rental(self):
        answer = input('would you like to rent a car? y/n')
        if answer == 'y':
            answer = input('what type would you like? p/e')
            amount = int(input('how many would you like?'))
            if answer == 'p':
                self.rent(self.petrol_cars, amount)
            else:
                self.rent(self.electric_cars, amount)
        self.stock_count()

def dealership_main():
    dealership_init()

    dealership = Dealership()
    dealership.create_current_stock()
    proceed = 'y'
    while proceed == 'y':
        dealership.process_rental()
        proceed = input('continue? y/n')