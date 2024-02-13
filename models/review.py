#!/usr/bin/python3
"""creates the user Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class for managing review obj.
    """

    place_id = ""
    user_id = ""
    text = ""
