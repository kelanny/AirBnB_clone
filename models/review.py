#!/usr/bin/python3
"""This module defines one Review model class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review for a place.

    Public Class Attributes:
        place_id (str): The ID of the associated place (default: empty string).
        user_id (str): The ID of the user who wrote the review.
        text (str): The text content of the review (default: empty string).
    """
    place_id = ""
    user_id = ""
    text = ""
