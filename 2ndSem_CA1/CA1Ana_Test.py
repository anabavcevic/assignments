import unittest
from bs4 import BeautifulSoup

from CA1Ana_Functions import *


# test the car functionality
class TestCA1Ana(unittest.TestCase):

    def test_extract_island(self):
        cell = BeautifulSoup('<td><a href="/wiki/Krk" title="Krk">The isle of Krk</a></td>', 'html.parser')
        actual = extract_island(cell)
        
        self.assertEqual("The isle of Krk", actual)
        
        
    def test_extract_population(self):
        cell = BeautifulSoup('<td><span data-sort-value="70041552" >15,522</span></td>', 'html.parser')
        actual = extract_population(cell)
        
        self.assertEqual("15522", actual)
        
        
    def test_extract_area(self):
        cell = BeautifulSoup('<td><span data-sort-value="70041552" ></span>405.78&nbsp;km<sup>2</sup> (100,270 acres)</td>', 'html.parser')
        actual = extract_area(cell)
        
        self.assertEqual("405.78", actual)
        
        
    def test_higest_point(self):
        cell = BeautifulSoup('<td><span data-sort-value="70041552" ></span>568&nbsp;m (1,864&nbsp;ft)</td>', 'html.parser')
        actual = extract_higest_point(cell)
        
        self.assertEqual("568", actual)
        
    def test_population_density(self):
        cell = BeautifulSoup('<td><span data-sort-value="70041552" ></span>47.8/km<sup>2</sup> (0.193/acre)</td>', 'html.parser')
        actual = extract_population_density(cell)
        
        self.assertEqual("47.8", actual)
        
        

if __name__ == '__main__':
    unittest.main()
