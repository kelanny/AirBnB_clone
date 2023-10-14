import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_attributes(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsNotNone(self.base_model.created_at)
        self.assertIsNotNone(self.base_model.updated_at)

    def test_save_method(self):
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        updated_at_after_save = self.base_model.updated_at
        self.assertNotEqual(initial_updated_at, updated_at_after_save)

    def test_to_dict_method(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.base_model.updated_at.isoformat())

    def test_str_method(self):
        obj_str = str(self.base_model)
        self.assertIn('BaseModel', obj_str)
        self.assertIn(self.base_model.id, obj_str)

if __name__ == '__main__':
    unittest.main()

