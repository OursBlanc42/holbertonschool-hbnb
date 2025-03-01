import unittest
from app import create_app


class TestPlaceEndpoints(unittest.TestCase):

    def setUp(self):
        """Set up test client and create a user for testing"""
        self.app = create_app()
        self.client = self.app.test_client()


        user_response = self.client.post('/api/v1/users/', json={
            "first_name": "Luke",
            "last_name": "Skywalker",
            "email": "luke.skywalker@starwars.com"
        })
        self.assertEqual(user_response.status_code, 201)
        self.user_id = user_response.json['id']


        place_response = self.client.post('/api/v1/places/', json={
            "title": "Tattoine hut",
            "description": "A place with 3 suns to stay",
            "price": 100.42,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner": self.user_id
        })
        self.assertEqual(place_response.status_code, 201)
        self.place_id = place_response.json['id']

    def test_get_place(self):
        """Test retrieving a specific place"""
        response = self.client.get(f'/api/v1/places/{self.place_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], self.place_id)
        self.assertEqual(response.json['title'], "Tattoine hut")
        self.assertEqual(response.json['description'], "A place with 3 suns to stay")
        self.assertEqual(response.json['price'], 100.42)
        self.assertEqual(response.json['latitude'], 37.7749)
        self.assertEqual(response.json['longitude'], -122.4194)
        self.assertEqual(response.json['owner'], self.user_id)

    def test_create_place(self):
        """Test creating a new place with valid data"""
        response = self.client.post('/api/v1/places/', json={
            "title": "Dagobah swamp",
            "description": "Yoda's home",
            "price": 1337.00,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner": self.user_id
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)
        self.assertEqual(response.json['title'], "Dagobah swamp")
        self.assertEqual(response.json['price'], 1337.00)

    def test_create_place_no_data(self):
        """Test creating a new place with no data"""
        response = self.client.post('/api/v1/places/', json={})
        self.assertEqual(response.status_code, 400)

    def test_create_place_invalid_data(self):
        """Test creating a new place with invalid data"""
        response = self.client.post('/api/v1/places/', json={
            "title": "Tattoine hut",
            "description": "A place with 3 suns to stay",
            "price": "100.42",
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner": self.user_id
        })
        self.assertEqual(response.status_code, 400)

    def test_get_places(self):
        """Test retrieving all places"""
        response = self.client.get('/api/v1/places/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_get_place_not_found(self):
        """Test retrieving a place that does not exist"""
        response = self.client.get('/api/v1/places/non-existent-id')
        self.assertEqual(response.status_code, 404)

    def test_update_place(self):
        """Test updating a place"""
        response = self.client.put(f'/api/v1/places/{self.place_id}', json={
            "title": "Dagobah cave",
            "price": 13.37,
            "description": "A place to face your fears"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['title'], "Dagobah cave")
        self.assertEqual(response.json['price'], 13.37)
        self.assertEqual(response.json['description'], "A place to face your fears")

    def test_update_place_not_found(self):
        """Test updating a place that does not exist"""
        response = self.client.put('/api/v1/places/non-existent-id', json={
            "title": "Dagobah cave"
        })
        self.assertEqual(response.status_code, 404)

    def test_update_place_invalid_data(self):
        """Test updating a place with invalid data"""
        response = self.client.put(f'/api/v1/places/{self.place_id}', json={
            "price": "petit prix :)"  # Price should be a number
        })
        self.assertEqual(response.status_code, 400)

"""
Because Ewoks should not exist

    def test_delete_place(self):
        Test deleting a place
        temp_place = self.client.post('/api/v1/places/', json={
            "title": "Endor forest",
            "description": "Home of the Ewoks, must be deleted",
            "price": 13.37,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner": self.user_id
        })
        temp_id = temp_place.json['id']

        response = self.client.delete(f'/api/v1/places/{temp_id}')
        self.assertEqual(response.status_code, 204)

        get_response = self.client.get(f'/api/v1/places/{temp_id}')
        self.assertEqual(get_response.status_code, 404)

    def test_delete_place_not_found(self):
        Test deleting a place that does not exist
        response = self.client.delete('/api/v1/places/non-existent-id')
        self.assertEqual(response.status_code, 404)
"""
