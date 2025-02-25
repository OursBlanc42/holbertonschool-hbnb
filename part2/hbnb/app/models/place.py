#!/usr/bin/python3
"""
Module for place
"""

from app.models.base_model import BaseModel


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        """
        Create instance of a place

        Args:
            title (string): Title of the place
            description (string): Description of the place
            price (float): Price of the place
            latitude (float): Latitude (geoloc) of the place
            longitude (float): Longitude (geoloc) of the place
            owner (user): Owner of the place
        """
        super().__init__()  # Call parent to generate UUID & timestamps
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
