#!/usr/bin/python3

"""This module defines BaseModel class."""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Represent the BaseModel of the whole program.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a BaseModel instance.

        Args:
            *args (any): Unused
            **kwargs: A dictionary with attributes and their values.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        dt_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue

                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, dt_format)

                setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self):
        """Updates the public instance attr updated_at with current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dict containing all keys/values of dict of the instance.
        """

        self.obj_dict = self.__dict__.copy()
        self.obj_dict["__class__"] = self.__class__.__name__
        self.obj_dict["created_at"] = self.created_at.isoformat()
        self.obj_dict["updated_at"] = self.updated_at.isoformat()
        return (self.obj_dict)

    def __str__(self):
        """Print the string representation of BaseModel instance.
        """
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))
