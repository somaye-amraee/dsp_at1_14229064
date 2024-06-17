import datetime
import sys

def check_arguments(args):
    """
    --------------------
    Description
    --------------------
    -> check_arguments (function): Function that will check if there are enough input arguments provided (ie exactly 3) 
    and will return the input arguments if it is the case.
    -> Otherwise the program will exit and display the relevant message provided in the assignment brief

    --------------------
    Parameters
    --------------------
    None

    --------------------
    Pseudo-Code
    --------------------
    It is checking whether the user inputs three appropriate arguments (<date> <post_code> <country_code>) or no? If no, the related error message wil be printed.

    --------------------
    Returns
    --------------------
    None

    """
    # => To be filled by student
    if len(args) != 3:
        print("[ERROR] You need to provide 3 arguments in the following order: <date> <post_code> <country_code>")
        sys.exit(0)
    else:
        return True

def check_date(date):
    """
    --------------------
    Description
    --------------------
    -> check_date (function): Function that will check if the provided date is valid (YYYY-MM-DD format) and will return the value True if that is the case. 
    -> Otherwise the program will exit and display the relevant message provided in the assignment brief

    --------------------
    Parameters
    --------------------
    


    none

    --------------------
    Pseudo-Code
    --------------------
    This function checks whether the format of intered date is valid or not?  If the format is like YYYY-MM-DD, the return value would be True,
    otherwise a message of "Provided date is invalid" will be printed and the program will exit.

    --------------------
    Returns
    --------------------
    None

    """
    # => To be filled by student
    try:
        if date != datetime.datetime.strptime(date, "%Y-%m-%d").strftime('%Y-%m-%d'):
            raise ValueError
        return True
    except ValueError:
        print("Provided date is invalid")
        return False
        sys.exit(0)