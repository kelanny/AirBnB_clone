#!/usr/bin/python3
"""This module contain one class User that represent the User.
"""


class User(BaseModel):
    """User class that inherits from BaseModel.

    Attributes:
    - email (str): User's email address.
    - password (str): User's password.
    - first_name (str): User's first name.
    - last_name (str): User's last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
