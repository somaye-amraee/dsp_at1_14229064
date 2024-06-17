import unittest
from api import call_get

class TestAPI(unittest.TestCase):
    """
    Class used for testing the call_get() function in api.py
    """
    # => To be filled by student
    def test_api(self):
        self.test_url = "https://www.zippopotam.us"
        self.api_name = "/us/90210"
        self.assertNotEqual(call_get(self.test_url,str(self.api_name)), None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
