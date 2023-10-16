import unittest
from models.amenity import Amenity

class TestAmenityModel(unittest.TestCase):
    def test_amenity_inherits_from_base_model(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_amenity_default_name(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()

