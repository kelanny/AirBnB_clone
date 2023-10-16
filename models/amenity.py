#!/usr/bin/python3
"""This module defines one Amenity class."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity or feature of a place.

    Public Class Attributes:
    - name (str): The name of the amenity (default: empty string).
    """
    name = ""
