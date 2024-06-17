import sys
from places import Place
from checks import check_arguments, check_date

if __name__ == "__main__":
    """
    Main logics of the program.

    Pseudo-code
    ----------
    Extract the input arguments
    Remove the first argument (name of Python script)
    Check there are 3 items in the remaining list of argument (using your defined check_arguments() function)
    Check the validity of the input date (using your defined check_date() function)
    Instantiate an objet from your defined Place class with the country and post codes and date
    Extract the relevant information from the Zippopotam and Sunrise-Sunset APIs using your instantiated Place object
    Display the expected output message using your instantiated Place object
    """
    # => To be filled by student

    

    args = sys.argv[1:]

    if check_arguments(args):
        country_code = args[2] 
        post_code = args[1]  
        date = args[0]

        if check_date(date):
            place_info = Place(country_code=country_code,  post_code=post_code, date=date)
            place_info.extract_apis_information()
            place_info.display_output()
            
            
