from api import call_get

class SunriseSunset:
    """
    --------------------
    Description
    --------------------
    -> SunriseSunset (class): Class that manages API calls to Sunrise-Sunset.
     It will be used to store the URL to the relevant endpoint,
     extract and store information for the program.

    --------------------
    Attributes
    --------------------
    -> base_url (str): Base url to Zippopotam API (optional)
    -> date (str): Date of interest (mandatory)
    -> place_lat (float): Latitude value of location of interest (mandatory)
    -> place_lon (float): Longitude value of location of interest (mandatory)
    -> api_response (dict): Results returned from API call (optional)
    -> status (str): Status returned by API (optional)
    -> sunrise_utc (str): UTC Time of sunrise for location of interest for a given date (optional)
    -> sunset_utc (str): UTC Time of sunset for location of interest for a given date (optional)
    """
    def __init__(self, date, place_lat, place_lon):
        self.base_url: str = 'https://api.sunrise-sunset.org/json'
        self.date = str(date)
        self.place_lat = str(place_lat)
        self.place_lon = str(place_lon) 
        self.api_response = None
        self.status = None
        self.sunrise_utc = ""
        self.sunset_utc = ""

    def get_place_result(self):
        """
        --------------------
        Description
        --------------------
        -> get_place_result (method): Method that will call the Sunrise-Sunset API endpoint and save the results as a dictionary (self.api_response).

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        It will store the results of self.api_response dictionary from calling the Sunrise-Sunset API endpoint

        --------------------
        Returns
        --------------------
        None
        """
        # => To be filled by student
        str_request = f'?lat={self.place_lat}&lng={self.place_lon}&date={self.date}'
        self.api_response = call_get(self.base_url, str_request)
        if self.api_response != None:
            return self.api_response
        else:
            return False


    def store_place_sun_information(self):
        """
        --------------------
        Description
        --------------------
        -> store_place_sun_information (method): Method that will extract information from a dictionary (self.api_response) and 
        store each individual information into the relevant attributes (status, sunrise_utc, sunset_utc).

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        It will extract information from self.api_response and extract some information and store them in the related attributes.

        --------------------
        Returns
        --------------------
        None
        """
        # => To be filled by student
        self.api_response= self.get_place_result()
        self.status = self.api_response["status"]
        self.sunrise_utc = self.api_response["results"]["sunrise"]
        self.sunset_utc = self.api_response["results"]["sunset"]
        return [self.sunrise_utc, self.sunset_utc] 


    def check_status(self):
        """
        --------------------
        Description
        --------------------
        -> check_status (method): Method that will check the status of the API call and return an error message if status is not OK. Otherwise it returns None

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        It checks whether status of the API call is OK or not.

        --------------------
        Returns
        --------------------
        None
        """
        # => To be filled by student
        if self.status != "OK":
            return('the status is not ok')
        else:
            return None


