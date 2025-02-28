from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(
        required=True,
        description='Text of the review'
    ),
    'rating': fields.Integer(
        required=True,
        description='Rating of the place (1-5)',
        min=1,
        max=5
    ),
    'user_id': fields.String(
        required=True,
        description='ID of the user'
    ),
    'place_id': fields.String(
        required=True,
        description='ID of the place'
    )
})

# Define the review model for "update operation" (without place and user UUID)
review_update_model = api.model('ReviewUpdate', {
    'text': fields.String(
        required=True,
        description='Text of the review'
    ),
    'rating': fields.Integer(
        required=True,
        description='Rating of the place (1-5)',
        min=1,
        max=5
    )
})


@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model, validate=True)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """
        Register a new review

        Returns:
        tuple: A tuple containing:
            - dict: A dictionary with either the created review
            details or an error message
            - int: HTTP status code
            (201 if successful, 400 if there is an error)
        """
        review_data = api.payload

        # Check if user UUID exist
        users = facade.get_all_users()
        for users_item in users:
            if users_item.id == review_data['user_id']:
                break
        else:
            return {'message': "The given user UUID does not exist"}, 400

        # Check if place UUID exist (commented because waiting place implementation)
        """
        places = facade.get_all_places()
        for places_item in places:
            if places_item.id == review_data['place_id']:
                break
        else:
            return {'message': "The given place UUID does not exist"}, 400
        """

        new_review = facade.create_review(review_data)
        return {
            'id': new_review.id,
            'text': new_review.text,
            'rating': new_review.rating,
            'user_id': new_review.user_id,
            'place_id': new_review.place_id
            }, 201

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """
        Get the list of all reviews

        Returns:
            tuple: A tuple containing:
                - list: A list of dictionnaries, each containing review data
                - int: HTTP status code 200 for success
        """
        reviews = facade.get_all_reviews()
        return [
            {
                'id': review_item.id,
                'text': review_item.text,
                'rating': review_item.rating,
            }
            for review_item in reviews
        ], 200


@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """
        Get review details by ID.

        Args:
            review_id (UUID): The ID of the review to retrieve details for

        Returns:
            tuple: A tuple containing:
                - dict: A dictionary with either the usreviewer data
                or an error message.
                - int: HTTP status code (200 if successful, 404 if not found)
        """
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        return {
            'id': review.id,
            'text': review.text,
            'rating': review.rating,
            'user_id': review.user_id,
            'place_id': review.place_id
        }, 200

    @api.expect(review_update_model, validate=True)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """
        Update review details by ID.

        Args:
            review_id (UUID): The ID of the user to be updated

        Returns:
            tuple: A tuple containing:
                - dict: A dictionary with either the review data
                or an error message.
                - int: HTTP status code
                (200 if successful, 400 or 404 if error)
        """
        review_data = api.payload

        review = facade.update_review(review_id, review_data)
        if not review:
            return {"error": "Review not found"}, 404
        else:
            return {"Message": "Review updated successfully"}, 200

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """
        Delete review by ID.

        Args:
            review_id (UUID): The ID of the user to be deleted

        Returns:
            tuple: A tuple containing:
                - dict: A dictionary with information message
                - int: HTTP status code
                (200 if successful, 404 if error)
        """

        # Check if review exist and delete it
        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        else:
            facade.delete_review(review_id)
            return {"message": "Review deleted successfully"}, 200


@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        # Placeholder for logic to return a list of reviews for a place
        pass
