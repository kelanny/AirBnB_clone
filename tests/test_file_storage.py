#!/usr/bin/python3
"""Unittest module for file_storage.py"""

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = "test_data.json"
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.base_model.save()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_initialization(self):
        self.assertEqual(self.storage._FileStorage__file_path, "data.json")
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all_method(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertIn('BaseModel.{}'.format(self.base_model.id), all_objects)
        self.assertEqual(
                    all_objects['BaseModel.{}'
                            .format(self.base_model.id)], self.base_model
                    )

    def test_new_method(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        all_objects = self.storage.all()
        self.assertIn('BaseModel.{}'.format(new_model.id), all_objects)
        self.assertEqual(all_objects['BaseModel.{}'
                            .format(new_model.id)], new_model)

    def test_save_and_reload_methods(self):
        # Save the data to a temporary file
        self.storage.save()

        # Create a new storage instance
        new_storage = FileStorage()

        # Check that the file doesn't exist in the new instance
        self.assertFalse(os.path.exists(self.file_path))

        # Reload data from the temporary file
        new_storage.reload()

        # Check that the data was loaded correctly
        all_objects = new_storage.all()
        self.assertIn('BaseModel.{}'.format(self.base_model.id), all_objects)
        self.assertEqual(all_objects['BaseModel.{}'
            .format(self.base_model.id)].to_dict(), self.base_model.to_dict())


if __name__ == '__main__':
    unittest.main()
