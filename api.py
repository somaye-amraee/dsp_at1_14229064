import requests
import sys


url = 'https://www.zippopotam.us' # url of the website

def call_get(url: str, api_name: str) -> requests.models.Response:
    """
    --------------------
    Description
    --------------------
    -> call_get (method): Function that will call the API endpoint (input parameter) and return its response as a requests.models.Response object
    -> In case of an error, the program will exit and display the relevant message provided in the assignment brief

    --------------------
    Parameters
    --------------------
    url: str,
    api_name: str

    --------------------
    Pseudo-Code
    --------------------
    A function that will call the relevant api and return its response.
    If there would be an error, the meassage 'There is an error with zippotam API' would be printed. 

    --------------------
    Returns
    --------------------
    None
    """

    url_final = f'{url}{api_name}'

    response = requests.get(url_final)

    if response.status_code==200:

        return response.json()

    else:

        print("There is an error with zippotam API")
        return None
    

