#!/usr/bin/python3
"""
    This module contains one class FileStorage.
    Serializes class instances to JSON file.
    Desiarializes JSON file to instances.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
        Serializes instances to a JSON file and deserializes it to instances.

    Private class attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dict - empty but will store all objects by <class name>.id
            (
                ex: to store a BaseModel object with id=12121212,
                    the key will be BaseModel.12121212
            )
    Public instance methods:
        - all(self): returns the dictionary __objects
        - new(self, obj): sets in __objs the obj with key <obj class name>.id
        - save(self): serializes __objects to the JSON file (path: __file_path)
        - reload(self): deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists ;
                otherwise, do nothing. If the file doesn’t exist,
                no exception should be raised
            )

    """
    __file_path = "data.json"
    __objects = {}

    def __init__(self):
        """Initializes the FileStorage class instance.

        Args:
            __file_path: string - path to the JSON file (ex: file.json)
            __objects: dict - empty but will store all objs by <class name>.id
                (
                    ex: to store a BaseModel object with id=12121212,
                    the key will be BaseModel.12121212
                )

        """

    def all(self):
        """Return the dictionary objects
        """
        return (FileStorage.__objects)

    def new(self, obj):
        """Sets in __objects, the obj with given key.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objs to the JSON File in path (path: __file_path)
        """
        serialized = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name == "BaseModel":
                        obj = BaseModel(**obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

