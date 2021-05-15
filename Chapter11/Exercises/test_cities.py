import unittest
from Chapter11.Exercises.city_functions import get_formatted_city_name


class CityNamesTestCase(unittest.TestCase):
    """Test for city_functions.py"""

    def test_city_country(self):
        formatted_name = get_formatted_city_name('santiago', 'chile')
        self.assertEqual(formatted_name, "Santiago, Chile")


if __name__ == '__main__':
    unittest.main()
