#from curses.ascii import US
import unittest
from unittest.mock import patch
from io import StringIO
from api_zippopotam import Zippopotam


class TestZippopotamInstantiation(unittest.TestCase):
    """
    Class used for testing the instanciation of the Zippopotam class from api_zippopotam.py
    """
    def test_Instantiation_Zippopptam(self):
        self.exp_country_code = 'US'
        self.exp_post_code = '90210'
        self.assertEqual (self.exp_country_code, Zippopotam ( 'US', '90210').country_code)
        self.assertEqual (self.exp_post_code, Zippopotam ( 'US', '90210').post_code)
         

class TestZippopotam_get_place_result(unittest.TestCase):
    """
    Class used for testing the Zippopotam.get_place_result() method from api_zippopotam.py
    """
    def test_get_place_results(self):
        
        self.exp_response: dict = {'post code': '90210', 'country': 'United States', 'country abbreviation': 'US', 'places': [{'place name': 'Beverly Hills', 'longitude': '-118.4065', 'state': 'California', 'state abbreviation': 'CA', 'latitude': '34.0901'}]}
        self.assertEqual(self.exp_response, Zippopotam ( 'US', '90210').get_place_result())

class TestZippopotam_store_place_information(unittest.TestCase):
    """
    Class used for testing the Zippopotam.store_place_information() method from api_zippopotam.py
    """
    def test_store_place_infomation(self):
       zip = Zippopotam('US','90210')
       zip.api_response = {'post code': '90210', 'country': 'United States', 'country abbreviation': 'US', 'places': [{'place name': 'Beverly Hills', 'longitude': '-118.4065', 'state': 'California', 'state abbreviation': 'CA', 'latitude': '34.0901'}]}
       self.exp_response = ['United States','Beverly Hills', 'California', '34.0901', '-118.4065']
       self.assertEqual(self.exp_response, zip.store_place_information())


if __name__ == '__main__':
    unittest.main(verbosity=2)