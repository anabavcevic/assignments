import finalcars
import unittest

from collections import namedtuple


class TestRentedItemMixin(unittest.TestCase):
    def testGetSetRented(self):
        for test_case in [True, False]:
            rim = finalcars.RentedItemMixin()
            # Default value must be False.
            self.assertFalse(rim.getRented())
            # Set the value and veirfy returned value matches.
            rim.setRented(test_case)
            self.assertEqual(rim.getRented(), test_case)

    def testRentOut(self):
        rim = finalcars.RentedItemMixin()
        # Default value must be False.
        self.assertFalse(rim.getRented())
        # Renting out the car changes the value.
        rim.rentOut()
        self.assertTrue(rim.getRented())
        # Renting out the car again changes nothing.
        rim.rentOut()
        self.assertTrue(rim.getRented())

    def testReturned(self):
        rim = finalcars.RentedItemMixin()
        # Default value must be False.
        self.assertFalse(rim.getRented())
        # Returning a car that is not rented, changes nothing.
        rim.returned()
        self.assertFalse(rim.getRented())
        # Returning a car that was marked rented, changes the status.
        rim.setRented(True)
        self.assertTrue(rim.getRented())
        rim.returned()
        self.assertFalse(rim.getRented())


class CommonCarTestCase(unittest.TestCase):
    def assertCarData(self, data, cls_under_test):
        self.assertEqual(data.colour, cls_under_test.getColour())
        self.assertEqual(data.make, cls_under_test.getMake())


class TestImpElectricCar(CommonCarTestCase):
    def testLoadData(self):
        # Construct a named tuple with required fields.
        DataTuple = namedtuple("DataTuple", ['num_cells', 'colour', 'make'])
        data = DataTuple(
            colour='Red',
            make='Nissan Leaf',
            num_cells=12,
            )
        # Load the data into the new instance of ImpElectricCar.
        iec = finalcars.ImpElectricCar()
        iec.loadData(data)
        # Verify the outputs are correct.
        self.assertEqual(data.num_cells, iec.getNumberFuelCells())
        self.assertCarData(data, iec)


class TestICECar(CommonCarTestCase):
    def testLoadData(self):
        # Construct a named tuple with required fields
        DataTuple = namedtuple("DataTuple", ['fuel_type', 'num_cylinders', 'colour', 'make'])
        data = DataTuple(
            fuel_type='petrol',
            num_cylinders=4,
            colour='Blue',
            make='Pegueot 206',
        )
        # Load the data into a new instance of ICECar.
        ic = finalcars.ICECar()
        ic.loadData(data)
        # Verify the outputs are correct.
        self.assertEqual(data.fuel_type, ic.getFuelType())
        self.assertEqual(data.num_cylinders, ic.getNumberCylinders())
        self.assertCarData(data, ic)


class TestHybridCar(CommonCarTestCase):
    def testLoadData(self):
        # Construct a named tuple with required fields
        DataTuple = namedtuple(
            "DataTuple",
            ['num_cells', 'fuel_type', 'num_cylinders', 'colour', 'make'])
        data = DataTuple(
            num_cells=16,
            fuel_type='petrol',
            num_cylinders=4,
            colour='Blue',
            make='BMW i3',
        )
        # Load the data into a new instance of ICECar.
        hc = finalcars.HybridCar()
        hc.loadData(data)
        # Verify the outputs are correct.
        self.assertEqual(data.num_cells, hc.getNumberFuelCells())
        self.assertEqual(data.fuel_type, hc.getFuelType())
        self.assertEqual(data.num_cylinders, hc.getNumberCylinders())
        self.assertCarData(data, hc)


if __name__ == '__main__':
    unittest.main()