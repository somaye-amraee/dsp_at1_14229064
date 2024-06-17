Project title: Building a Sunrise/Sunset Finder in Python

## Author
Name: Somayeh Amraee - Student ID: 14229064


## Description
<What your application does>
This python program that will look for the sunrise and sunset times (UTC) for a specific location at a given date.
<Some of the challenges you faced>
I faced problems in debugging the code and I learned about the unittest module and some general python programming.
<Some of the features you hope to implement in the future>
I would like to make this application more interactive and user_friendly.
To be more precise, it asks the user how to enter inputs in a dynamic screen. To do so the thinker library might be needed.




## How to Setup
<Provide a step-by-step description of how to get the development environment set and running.>
Open the terminal and enter the command :
python main.py <date> <post_code> <country_code>  like: python main.py 2022-10-04 90210 US 
The output would be like: On 2022-10-04, the sunrise and sunset time for Beverly Hills 90210 in California, United States were respectively at 1:35:08 AM and 1:49:20 PM (UTC time)

<Which Python version you used> : Python 3.10.8
<Which packages and version you used> altair==4.2.0, requests:2.28.1, sys, datetime




## How to Run the Program
<Provide instructions and examples>
Here is the command for running the script:
python main.py <date> <post_code> <country_code>
For example enter: python main.py 2022-10-04 90210 US
The output: On 2022-10-04, the sunrise and sunset time for Beverly Hills 90210 in California, United States were respectively at 1:35:08 AM and 1:49:20 PM (UTC time)
If you enter a comment which has a missing argument like: python main.py 2022-10-04 90210
The output would be: [ERROR] You need to provide 3 arguments in the following order: <date> <post_code> <country_code>
or if you enter a comment which <date> <post_code> <country_code> are missed like: python main.py 2022-10-04 90210
the output would be like: 
The output would be: [ERROR] You need to provide 3 arguments in the following order: <date> <post_code> <country_code>





## Project Structure
<List all folders and files of this project and provide quick description for each of them>
There is just one folder (dsp_at1_14229064) including following files:

- README.md: 
A file providing important information about the project such project description, project structure, setup and running the project guide, citations, etc.

- requirements.txt: 
A list of all packages required to run the project. The file is used by pip to install.

- api.py 
There is a function in this module that will call the API endpoint (input parameter = url) and return its response as a requests.models.Response object
In case of an error, the program will exit and display the relevant message "There is an error with zippotam API"

- api_sunrisesunset.py 
Python script that includes the class used for calling relevant Sunrise-Sunset endpoints

- api_zippopotam.py
This is a module which is include Zippopotam class that manages API calls to Zippopotam. 
It will be used to store the URLS to the relevant endpoints. 


- checks.py
This module check the validity of input arguments and dates in check_arguments and check_date methods>

- main.py
main program used for running the business logics

- places.py
python script that will contain the class used for extracting place information and dates of sunrise and sunset 

- test_api.py 
Unit tests for api.py
- test_api_sunrisesunset_ASO.py
Unit tests for sunrisesunset_ASO.py
- test_api_zippopotam_ASO.py
Unit tests for api_zippopotam_ASO.py
- test_checks.py
Unit tests for checks.py
- test_places.py
Unit tests for places.py


## Citations
<Mention authors and provide links code you source externally>
- Read the docs from Python unittest to use Mock for testing:
  https://docs.python.org/3/library/unittest.mock.html
  https://www.zippopotam.us/
  https://sunrise-sunset.org/

