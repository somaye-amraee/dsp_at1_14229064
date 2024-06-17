import unittest
from checks import check_arguments, check_date


class TestCheckArguments(unittest.TestCase):
    """
    Class used for testing the check_arguments() function from checks.py
    """
    # => To be filled by student
    def test_check_arguments(self):
        self.args = '2022-10-18', '90210', 'US'
        self.assertTrue(check_arguments(self.args))


class TestCheckDate(unittest.TestCase):
    """
    Class used for testing the check_date() function from checks.py
    """
    # => To be filled by student
    def test_check_date(self):
        date = "2022-01-01"
        self.assertTrue(check_date(date))

    def test_check_date_false(self):
        date = "2000-30-01"
        self.assertFalse(check_date(date))


if __name__ == '__main__':
    unittest.main(verbosity=2)