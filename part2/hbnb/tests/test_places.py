import unittest
from app import create_app


class TestPlaceEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user(self):
        """
        Test creating a new place with valid data

        Due to the creation of a random UUID for each user, we need to
        create a user first, then retrieve it to create the place
        """

        response = self.client.post('/api/v1/users/', json={
            "first_name": "Luke",
            "last_name": "Skywalker",
            "email": "luke.skywalker@starwars.com"
        })
        self.assertEqual(response.status_code, 201)

        # Get user ID from response
        user_id = response.json['id']

        response = self.client.post('/api/v1/places/', json={
            "title": "Tattoine hut",
            "description": "A place with 3 suns to stay",
            "price": 100.42,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner": user_id
        })
        self.assertEqual(response.status_code, 201)
