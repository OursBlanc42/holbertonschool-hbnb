from app.persistence.repository import InMemoryRepository
from app.models.user import User

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_all_users(self):
        users = self.user_repo.get_all()
        return users

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass

    def update_user(self, user_id, user_data):
        """
        update_user

        Update user information base on user_id
        1 - Check if the user exist
        2 - Input are validated in 'put()' no need to recheck
        3 - Loop through user data and update data
        4 - Save the updated user in the repository

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
