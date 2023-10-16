#!/usr/bin/python3
"""This module define one City model"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city in a geographic location.

    Public Class Attributes:
    - state_id (str): The ID of the associated state (default: empty string).
    - name (str): The name of the city (default: empty string).
    """
    state_id = ""
    name = ""
