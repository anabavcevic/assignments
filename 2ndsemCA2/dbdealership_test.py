import dbdealership
import finalcars
import os
import unittest


_TESTDATA_PATH = 'testdata'


class TestLoadData(unittest.TestCase):
    def testICECarLoadData(self):
        data_path = os.path.join(_TESTDATA_PATH, 'ice.csv')
        cars = dbdealership.loadData(finalcars.ICECar, data_path)
        tests = (
            ('1', 'petrol', 4, 'Ford Focus', 'Red'),
            ('2', 'petrol', 4, 'Volkswagen Golf', 'Red'),
            ('3', 'petrol', 3, 'Ford Focus', 'White'),
            ('4', 'diesel', 3, 'Volkswagen Polo', 'White'),
        )
        self.assertEquals(len(cars), len(tests))
        for test in tests:
            car = cars.get(test[0])
            self.assertIsNotNone(car)
            self.assertEqual(car.getFuelType(), test[1])
            self.assertEqual(car.getNumberCylinders(), test[2])
            self.assertEqual(car.getMake(), test[3])
            self.assertEqual(car.getColour(), test[4])

    def testHybridCarLoadData(self):
        data_path = os.path.join(_TESTDATA_PATH, 'hybrid.csv')
        cars = dbdealership.loadData(finalcars.HybridCar, data_path)
        tests = (
            ('1', 15, 'petrol', 3, 'BMW i3', 'Blue'),
            ('2', 20, 'diesel', 4, 'Toyota Auris', 'Red'),
        )
        self.assertEquals(len(cars), len(tests))
        for test in tests:
            car = cars.get(test[0])
            self.assertIsNotNone(car)
            self.assertEqual(car.getNumberFuelCells(), test[1])
            self.assertEqual(car.getFuelType(), test[2])
            self.assertEqual(car.getNumberCylinders(), test[3])
            self.assertEqual(car.getMake(), test[4])
            self.assertEqual(car.getColour(), test[5])

    def testElectricCarLoadData(self):
        data_path = os.path.join(_TESTDATA_PATH, 'electric.csv')
        cars = dbdealership.loadData(finalcars.ImpElectricCar, data_path)
        tests = (
            ('1', 20, 'Toyota Prius', 'White'),
            ('2', 20, 'Toyota Prius', 'Yellow'),
        )
        self.assertEquals(len(cars), len(tests))
        for test in tests:
            car = cars.get(test[0])
            self.assertIsNotNone(car)
            self.assertEqual(car.getNumberFuelCells(), test[1])
            self.assertEqual(car.getMake(), test[2])
            self.assertEqual(car.getColour(), test[3])


class TestDealership(unittest.TestCase):
    pass