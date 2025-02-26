from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity


class HBnBFacade:
    """
    Facade class to interact between the application
    and different repositories.
    """
    def __init__(self):
        """
        __init__

        Initialize repositories for user, place, review, and amenity
        """
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

# USER ENDPOINTS
    def create_user(self, user_data):
        """
        create_user

        Create a new user and add it to the user repository

        Args:
            user_data (dict): A dictionary containing user data

        Returns:
            User: User model representing the newly created user
        """
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_all_users(self):
        """
        get_all_users

        Retrivies all users from the repo

        Returns:
            list: A list of all User objects
        """
        users = self.user_repo.get_all()
        return users

    def get_user(self, user_id):
        """
        get_user

        Get a user by their UUID

        Args:
            user_id (UUID): UUID of the user to retrieve

        Returns:
            User: The user object corresponding to the UUID
        """
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """
        get_user_by_email

        Get a user by their email

        Args:
            email (string): email of the user to retrieve

        Returns:
            User: The user object corresponding to the mail
        """
        return self.user_repo.get_by_attribute('email', email)

    def update_user(self, user_id, user_data):
        """
        update_user

        Update an existing user with new data if it exists
        (Validation handled in "put")

        Args:
            user_id (UUID): UUID
            user_data (dict): Dictionnary of data

        Returns:
            user (User): instance of the user
            None: if the user does not exist
        """

        user = self.user_repo.get(user_id)

        if not user:
            return None

        if user:
            for key, value in user_data.items():
                setattr(user, key, value)
            self.user_repo.update(user, user_data)
        return user

# AMENITY ENDPOINTS
    def create_amenity(self, amenity_data):
        """
        create_amenity

        Create an amenity instance and add it to the repository

        Args:
            amenity_data (dict): A dictionary containing amenity data

        Returns:
            Amenity: The newly created Amenity object
        """
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        """
        get_amenity

        Retrieve an amenity by its ID

        Args:
            amenity_id (UUID): The ID of the amenity to retrieve

        Returns:
            Amenity: The amenity object corresponding to the ID
        """
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        """
        get_all_amenities

        Retrieves all amenities from the repository

        Returns:
            list: A list of all Amenity objects
        """
        amenities = self.amenity_repo.get_all()
        return amenities

    def update_amenity(self, amenity_id, amenity_data):
        """
        update_amenity

        Update an existing amenity with new data if it exists
        (Validation handled in "put")

        Args:
            amenity_id (UUID): UUID of the amenity to update
            amenity_data (dict): Dictionary of data to update

        Returns:
            amenity (Amenity): Instance of the updated amenity
            None: If the amenity does not exist
        """
        amenity = self.amenity_repo.get(amenity_id)

        if not amenity:
            return None

        if amenity:
            for key, value in amenity_data.items():
                setattr(amenity, key, value)
            self.amenity_repo.update(amenity, amenity_data)
        return amenity
