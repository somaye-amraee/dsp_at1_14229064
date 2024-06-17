import unittest
from places import Place

class TestPlaceInstantiation(unittest.TestCase):
    """
    Class used for testing the instanciation of the Place class from places.py
    """
    def test_Instantiation_Place(self):
        
        self.exp_date = '2022-05-18'
        self.exp_country_code = 'US'
        self.exp_post_code = '90210'
        self.assertEqual (self.exp_date, Place("US", '90210', "2022-05-18").date)
        self.assertEqual (self.exp_country_code, Place("US", '90210', "2022-05-18").country_code)
        self.assertEqual (self.exp_post_code, Place("US", '90210', "2022-05-18").post_code)

class TestPlace_extract_apis_information(unittest.TestCase): 
    """
    Class used for testing the Place.extract_apis_information() method from places.py
    """
    def test_extract_apis_information(self):
        self.assertIsNone(Place("US", '90210', "2022-05-18").extract_apis_information())

    

class TestPlace_display_output(unittest.TestCase):
    """
    Class used for testing the Place.display_output() method from places.py
    """
    def test_display_output(self):
        Place("US", '90210', "2022-05-18").extract_apis_information()
        self.assertIsNone(Place("US", '90210', "2022-05-18").display_output())

    
    
if __name__ == '__main__':
    unittest.main(verbosity=2)