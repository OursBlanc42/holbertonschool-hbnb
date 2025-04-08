from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.reviews import api as reviews_ns, places_reviews_ns
from app.api.v1.places import api as places_ns
from app.api.v1.auth import api as login_ns
from app.api.v1.protected import api as protected_ns
from flask_jwt_extended import JWTManager
from app.extensions import db, bcrypt

# instanciate the jwt object
jwt = JWTManager()


def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:3000", "http://localhost:3000"])
    app.config.from_object(config_class)

    api = Api(app, version='1.0', title='HBnB API',
              description='HBnB Application API')

    # Register the differents namespace
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(places_reviews_ns, path='/api/v1/places')
    api.add_namespace(login_ns, path='/api/v1/auth')
    api.add_namespace(protected_ns, path='/api/v1')

    # Initialize bcrypt
    bcrypt.init_app(app)

    # initialize jwt
    jwt.init_app(app)

    # initialize db
    db.init_app(app)

    return app
