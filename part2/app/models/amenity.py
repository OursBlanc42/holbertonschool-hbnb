#!/usr/bin/python3
"""
Module for amenity
"""

from app.models.base_model import BaseModel


class Amenity(BaseModel):

    def __init__(self, name, description=""):
        """
        Create instance of Amenity

        Args:
            name (string): Name of the amenity
            description (str, optional): Amenity description. Defaults to "".
        """
        super().__init__()  # Call parent to generate UUID & timestamps
        self.name = name
        self.description = description
