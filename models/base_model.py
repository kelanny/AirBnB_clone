#!/usr/bin/python3

"""This module hosts one class model BaseModel.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """This class model defines all common attributes,
        methods for other classes.

    Attributes:
        id (str): A string-assign with uuid when instance is created.
        created_at (datetime): Assigned with the current datetime.
            when an instance is created.
        updated_at (datetime): Assign with the current datetime
            when instance is created.
            Will be updated anytime the object is changed.

    Public instance methods:
        save(self): Updates the 'updated_at' attr with the current datetime.
        to_dict(self): Returns dict containing all instance attributes.
            - set using __dict__
            - Set as the first step to serialization/deserialization process.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a BaseModel instance with the given dict representation.

        Args:
        **kwargs: A dictionary with attributes and their values.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue

                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
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
        """Print the class name, instance id and class dict representation.
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
