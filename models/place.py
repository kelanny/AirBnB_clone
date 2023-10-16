#!/usr/bin/python3
"""This module defines one Place model class."""
from models.base_model import BaseModel


class place(BaseModel):
    """
    Represents a place or accommodation.

    Public Class Attributes:
        city_id (str): The ID of the associated city (default: empty string).
        user_id (str): The ID of the associated user (default: empty string).
        name (str): The name of the place (default: empty string).
        description (str): A description of the place (default: empty string).
        number_rooms (int): The number of rooms in the place (default: 0).
        number_bathrooms (int): The number of bathrooms in the place
        max_guest (int): The maximum number of guests the place can accommodate
        price_by_night (int): The price per night for the place (default: 0).
        latitude (float): The latitude coordinate of the place (default: 0.0).
        longitude (float): The longitude coordinate of the place (default: 0.0)
        amenity_ids (list): List of amenity IDs associated with the place.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
