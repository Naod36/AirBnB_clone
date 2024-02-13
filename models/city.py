#!/usr/bin/python3
"""creates the user City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """class for managing city Obj.
    """

    state_id = ""
    name = ""
