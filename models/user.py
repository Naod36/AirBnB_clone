#!/usr/bin/python3
"""creates the user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """class for managing user obj.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
