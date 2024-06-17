from api import call_get

class Zippopotam:
    """
    --------------------
    Description
    --------------------
    -> Zippopotam (class): Class that manages API calls to Zippopotam.
     It will be used to store the URL to the relevant endpoint, extract and store information for the program.

    --------------------
    Attributes
    --------------------
    -> base_url (str): Base url to Zippopotam API (optional)
    -> country_code (str): Country code following "ISO-3166 alpha2" format (mandatory)
    -> post_code (str): Postcode of location of interest (mandatory)
    -> api_response (dict): Results returned from API call (optional)
    -> country_name (str): Country of location of interest (optional)
    -> place_name (str): Name of location of interest (optional)
    -> place_state (list): State of location of interest (optional)
    -> place_lat (float): Latitude value of location of interest (optional)
    -> place_lon (float): Longitude value of location of interest (optional)
    """
    def __init__(self, country_code, post_code):
        # => To be filled by student
        self.base_url = "https://www.zippopotam.us/"
        self.country_code = country_code
        self.post_code = post_code
        self.api_response = {}
        self.country_name = None
        self.place_name = None
        self.place_state = []
        self.place_lat = None
        self.place_lon = None

    def get_place_result(self):
        """
        --------------------
        Description
        --------------------
        -> get_place_result (method): Method that will call the Zippopotam API endpoint and save the results as a dictionary (self.api_response).

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        It call the relevant api endpoint and save the resulted country code and post code as a dictionary in self.api_response

        --------------------
        Returns
        --------------------
        None
        """
        # => To be filled by student
        # place_endpoint = self.zippopotam_url
        api_str = str('/' + self.country_code + '/' + self.post_code)
        self.api_response = call_get(self.base_url, api_str)
        return self.api_response

    def store_place_information(self):
        """
        --------------------
        Description
        --------------------
        -> store_place_information (method): Method that will extract information from a dictionary (self.api_response) and store each individual information into the relevant attributes 
        (api_response, country_name, place_name, place_state, place_lat, place_lon).
        -> If multiple places are returned from the API, only the first one will be used.

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        It extract post code, country, place name, state, longitude,  latitude from the dictionary of self.api_response and store each of the mentioned information in a relevant attribute. 

        --------------------
        Returns
        --------------------
        None
        """
        sar  = self.get_place_result()
        self.country_name = sar["country"]
        first_element = sar["places"][0]
        self.place_name = first_element["place name"]
        self.place_state = first_element["state"]
        self.place_lat = first_element["latitude"]
        self.place_lon = first_element["longitude"]
        return [self.country_name, self.place_name, self.place_state, self.place_lat, self.place_lon]
