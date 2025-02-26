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

    def validate_data(self, price, latitude, longitude):
        """
        Validate the data for a place

        Args:
            price (float): Price of the place
            latitude (float): Latitude (geoloc) of the place
            longitude (float): Longitude (geoloc) of the place

        Returns:
            bool: True if all data is valid, False otherwise
        """
        if not isinstance(price, float) or price < 0:
            return ValueError("Price must be a non-negative number")
        if not isinstance(latitude, float) or not (-90 <= latitude <= 90):
            return ValueError("Latitude must be a number between -90 and 90")
        if not isinstance(longitude, float) or not (-180 <= longitude <= 180):
            return ValueError(
                "Longitude must be a number between -180 and 180")
        return True

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    def to_dict(self):
        """Return a dictionary representation of the place."""
        place_dict = super().to_dict()
        place_dict.update({
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner': self.owner.to_dict(),
            'reviews': [r.to_dict() for r in self.reviews],
            'amenities': [a.to_dict() for a in self.amenities]
        })
        return place_dict

    def update(self, data):
        """Update the place with new data."""
        for key, value in data.items():
            if key != 'id' and key != 'created_at' and key != 'updated_at':
                setattr(self, key, value)
        return self
