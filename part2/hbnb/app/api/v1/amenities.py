from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})


@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        amenity_data = api.payload

        amenities = facade.get_all_amenities()
        for amenity_item in amenities:
            if amenity_item.name == amenity_data['name']:
                return {'error': 'Amenity already registered'}, 400

        new_amenity = facade.create_amenity(amenity_data)
        return {
            "id": new_amenity.id,
            "name": new_amenity.name
        }, 201

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        amenities = facade.get_all_amenities()

        return [
            {
                "id": amenity_item.id,
                "name": amenity_item.name
            }
            for amenity_item in amenities
        ], 200


@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': 'Amenity not found'}, 404
        else:
            return {
                "id": amenity.id,
                "name": amenity.name
            }, 200

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """
        Update and amenity's information

        Returns:
            amenity: amenity updated information
            None: if invalid input data
        """
        amenity_data = api.payload
        if not amenity_data or not isinstance(amenity_data, dict):
            return {"error": "Invalid input data"}, 400

        amenity = facade.update_amenity(amenity_id, amenity_data)
        if not amenity:
            return {"error": "Amenity not found"}, 404
        else:
            return {
                "id": amenity.id,
                "name": amenity.name
            }, 200
