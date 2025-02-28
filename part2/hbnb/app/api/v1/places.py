from flask_restx import Namespace, Resource, fields
from flask import request
from app.services import facade

api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(
        required=True,
        description='Title of the place'),
    'description': fields.String(
        description='Description of the place',
        ),
    'price': fields.Float(
        required=True,
        description='Price per night',
        float_precision=2,
        min=0,
        error_message='Price must be a positive number',
        ),
    'latitude': fields.Float(
        required=True,
        description='Latitude of the place',
        min=-90,
        max=90,
        error_message='Latitude must be a number between -90 and 90',
        ),
    'longitude': fields.Float(
        required=True,
        description='Longitude of the place',
        min=-180,
        max=180,
        error_message='Longitude must be a number between -180 and 180',
        ),
    'owner': fields.String(
        required=True,
        description='ID of the owner',
        ),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        data = api.payload
        try:
            # Validate that owner exists
            owner = facade.get_user(data['owner'])
            if not owner:
                return {'message': 'Owner not found'}, 400

            # Validate that all amenities exist
            for amenity_id in data['amenities']:
                if not facade.get_amenity(amenity_id):
                    return {'message': f'Amenity {amenity_id} not found'}, 400

            place = facade.create_place(data)
            return {
                'id': place.id,
                'title': place.title,
                'description': place.description,
                'price': place.price,
                'latitude': place.latitude,
                'longitude': place.longitude,
                'owner': place.owner.id if hasattr(place.owner, 'id') else place.owner,
                'amenities': [amenity.id if hasattr(amenity, 'id') else amenity for amenity in place.amenities]
            }, 201
        except ValueError as e:
            return {'message': str(e)}, 400

    @api.response(200, 'List of places retrieved successfully')

    def get(self):
        """Retrieve a list of all places"""
        places = facade.get_all_places()
        return [{
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'price': place.price,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner': place.owner.id if hasattr(place.owner, 'id') else place.owner,
            'amenities': [amenity.id if hasattr(amenity, 'id') else amenity for amenity in place.amenities]
        } for place in places], 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place_by_id(place_id)
        if place:
            return place, 200
        return {'message': 'Place not found'}, 404

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        data = api.payload
        try:
            # Validate that owner exists if changing owner
            if 'owner' in data:
                owner = facade.get_user(data['owner'])
                if not owner:
                    return {'message': 'Owner not found'}, 400

            # Validate that all amenities exist if changing amenities
            if 'amenities' in data:
                for amenity_id in data['amenities']:
                    if not facade.get_amenity(amenity_id):
                        return {'message': f'Amenity {amenity_id} not found'}, 400

            place = facade.update_place(place_id, data)
            if place:
                return {
                    'id': place.id,
                    'title': place.title,
                    'description': place.description,
                    'price': place.price,
                    'latitude': place.latitude,
                    'longitude': place.longitude,
                    'owner': place.owner.id if hasattr(place.owner, 'id') else place.owner,
                    'amenities': [amenity.id if hasattr(amenity, 'id') else amenity for amenity in place.amenities]
                }, 200
            return {'message': 'Place not found'}, 404
        except ValueError as e:
            return {'message': str(e)}, 400
