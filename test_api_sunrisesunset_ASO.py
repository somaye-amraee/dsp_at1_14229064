import unittest
from unittest.mock import patch
from io import StringIO
from api_sunrisesunset import SunriseSunset


class TestSunriseSunsetInstantiation(unittest.TestCase):
    """
    Class used for testing the instanciation of the SunriseSunset class from api_sunrisesunset.py
    """
    def test_Instantiation_SunriseSunset(self):
        self.exp_date = '2022-05-18'
        self.exp_place_lat = '34.0901'
        self.exp_place_lon = '-118.4065'
        self.assertEqual (self.exp_date, SunriseSunset ( '2022-05-18', '34.0901', '-118.4065').date)
        self.assertEqual (self.exp_place_lat, SunriseSunset ( '2022-05-18', '34.0901', '-118.4065').place_lat)
        self.assertEqual (self.exp_place_lon, SunriseSunset ( '2022-05-18', '34.0901', '-118.4065').place_lon)

class TestSunriseSunset_get_place_result(unittest.TestCase):
    """
    Class used for testing the SunriseSunset.get_place_result() method from api_sunrisesunset.py
    """
    def test_get_place_results(self):
        self.exp_response: dict = {"results":{"sunrise":"12:48:13 PM","sunset":"2:51:56 AM","solar_noon":"7:50:04 PM","day_length":"14:03:43","civil_twilight_begin":"12:21:42 PM","civil_twilight_end":"3:18:27 AM","nautical_twilight_begin":"11:47:46 AM","nautical_twilight_end":"3:52:23 AM","astronomical_twilight_begin":"11:11:24 AM","astronomical_twilight_end":"4:28:45 AM"},"status":"OK"} 
        self.assertEqual(self.exp_response, SunriseSunset ('2022-05-18', '34.090100', '-118.406500').get_place_result())

class TestSunriseSunset_store_place_sun_information(unittest.TestCase):
    """
    Class used for testing the SunriseSunset.store_place_sun_information() method from api_sunrisesunset.py
    """
    def test_store_place_sun_information(self):
        self.sunrc = SunriseSunset('2022-05-18', '34.090100', '-118.406500')
        self.sunrc.api_response: dict = {"results":{"sunrise":"12:48:13 PM","sunset":"2:51:56 AM","solar_noon":"7:50:04 PM","day_length":"14:03:43","civil_twilight_begin":"12:21:42 PM","civil_twilight_end":"3:18:27 AM","nautical_twilight_begin":"11:47:46 AM","nautical_twilight_end":"3:52:23 AM","astronomical_twilight_begin":"11:11:24 AM","astronomical_twilight_end":"4:28:45 AM"},"status":"OK"} 
        self.exp_response = ["12:48:13 PM" , "2:51:56 AM" ]
        self.assertEqual(self.exp_response, self.sunrc.store_place_sun_information()) 

class TestSunriseSunset_check_status(unittest.TestCase):
    """
    Class used for testing the SunriseSunset.check_status() method from api_sunrisesunset.py
    """
    def test_store_place_sun_information(self):
        self.sunrc = SunriseSunset('2022-05-18', '34.090100', '-118.406500')
        self.sunrc.api_response: dict = {"results":{"sunrise":"12:48:13 PM","sunset":"2:51:56 AM","solar_noon":"7:50:04 PM","day_length":"14:03:43","civil_twilight_begin":"12:21:42 PM","civil_twilight_end":"3:18:27 AM","nautical_twilight_begin":"11:47:46 AM","nautical_twilight_end":"3:52:23 AM","astronomical_twilight_begin":"11:11:24 AM","astronomical_twilight_end":"4:28:45 AM"},"status":"OK"} 
        self.sunrc.store_place_sun_information()
        self.assertIsNone(self.sunrc.check_status()) 

if __name__ == '__main__':
    unittest.main(verbosity=2)