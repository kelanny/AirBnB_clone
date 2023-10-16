import unittest
from models.place import Place

class TestPlaceModel(unittest.TestCase):
    def test_place_inherits_from_base_model(self):
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_place_default_city_id(self):
        place = Place()
        self.assertEqual(place.city_id, "")

    def test_place_default_user_id(self):
        place = Place()
        self.assertEqual(place.user_id, "")

    def test_place_default_name(self):
        place = Place()
        self.assertEqual(place.name, "")


if __name__ == '__main__':
    unittest.main()
