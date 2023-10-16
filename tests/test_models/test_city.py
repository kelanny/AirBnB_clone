import unittest
from models.city import City

class TestCityModel(unittest.TestCase):
    def test_city_inherits_from_base_model(self):
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_city_default_state_id(self):
        city = City()
        self.assertEqual(city.state_id, "")

    def test_city_default_name(self):
        city = City()
        self.assertEqual(city.name, "")

if __name__ == '__main__':
    unittest.main()
