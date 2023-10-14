#!/usr/bin/python3
"""Unittest for base_model.py"""

import unittest
from from models.base_model import BaseModel
from datetime import datetime

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

    def test_custom_init(self):
        custom_data = {
            'id': 'custom_id',
            'created_at': '2023-01-15T12:00:00.000000',
            'updated_at': '2023-01-15T12:30:00.000000',
            'other_attr': 'some_value'
        }

        base_model = BaseModel(**custom_data)
        self.assertEqual(base_model.id, 'custom_id')
        self.assertEqual(base_model.created_at, datetime(2023, 1, 15, 12, 0))
        self.assertEqual(base_model.updated_at, datetime(2023, 1, 15, 12, 30))
        self.assertEqual(base_model.other_attr, 'some_value')

if __name__ == '__main__':
    unittest.main()

