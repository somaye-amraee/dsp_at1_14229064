import sys
from datetime import datetime
from api_zippopotam import Zippopotam
from api_sunrisesunset import SunriseSunset

class Place:
    """
    --------------------
    Description
    --------------------
    -> Place (class): Class that represents a location object. It will be used to store the input arguments (country and post codes  and date)
     and also other information required (state, name, country, latitude, longitude).

    --------------------
    Attributes
    --------------------
    -> country_code (str): Country code following "ISO-3166 alpha2" format (mandatory)
    -> post_code (str): Postcode of location of interest (mandatory)
    -> date (str): Date of interest (mandatory)
    -> latlon_api (Zippopotam): Zippopotam class (optional)
    -> sun_api (SunriseSunset): Results returned from API call (optional)
    """
    def __init__(self, country_code, post_code, date):
        # => To be filled by student
        self.country_code = str(country_code)
        self.post_code =  str(post_code)
        self.date = str(date)
        self.latlon_api= ""
        self.sun_api= ""
        self.country_name = ""
        self.place_name = ""
        self.place_state= ""
        self.place_lat = ""
        self.place_lon = ""
        self.sunrise_utc = ""
        self.sunset_utc = ""
        self.result_zippopotam = []
        self.result_sunriseset = []

    def extract_apis_information(self):
        """
        --------------------
        Description
        --------------------
        -> extract_apis_information (method): Method that will instantiate a Zippopotam (self.latlon_api) and
         a SunriseSunset (self.sun_api) classes and extract information collected from the APIs.

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        This function stores the informations from  Zippopotam and SunriseSunset apis into the required variables.

        --------------------
        Returns
        --------------------
        None
        """
        # => To be filled by student
        
        zip = Zippopotam(self.country_code, self.post_code)
        zip.get_place_result()
        self.result_zippopotam = zip.store_place_information()
        self.country_name = self.result_zippopotam[0]
        self.place_state = self.result_zippopotam[2]
        self.place_name = self.result_zippopotam[1]
        self.place_lon = self.result_zippopotam[4]
        self.place_lat = self.result_zippopotam[3]
        sunrs = SunriseSunset(self.date, self.place_lat, self.place_lon)
        sunrs.get_place_result()
        self.result_sunriseset = sunrs.store_place_sun_information()
        self.sunrise_utc = self.result_sunriseset[0] 
        self.sunset_utc = self.result_sunriseset[1]
        
        
        
        
        

    def display_output(self):
        """
        --------------------
        Description
        --------------------
        -> display_output (method): Method that will analyse the results returned by the 2 APIs and display the expected output.

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        This method shows the returned outputs of Zippopotam and SunriseSunset apis which are expected.

        --------------------
        Returns
        --------------------
        None
        """
        # => To be filled by student 
        print(f"On {self.date}, the sunrise and sunset time for {self.place_name} {self.post_code} in {self.place_state}, {self.country_name} were respectively at {self.sunset_utc} and {self.sunrise_utc} (UTC time)"  
        )