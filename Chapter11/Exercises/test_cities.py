import unittest
from Chapter11.Exercises.city_functions import get_formatted_city_name


class CityNamesTestCase(unittest.TestCase):
    """Test for city_functions.py"""

    def test_city_country(self):
        formatted_name = get_formatted_city_name('santiago', 'chile')
        self.assertEqual(formatted_name, "Santiago, Chile")

    def test_city_country_population(self):
        formatted_name = get_formatted_city_name('santiago', 'chile', population=5_000_000)
        self.assertEqual(formatted_name, "Santiago, Chile - population 5000000.")


if __name__ == '__main__':
    unittest.main()
