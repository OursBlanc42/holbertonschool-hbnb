from app import create_app
from app.services import facade


def create_admin_user():
    """
    Create an admin user in repostiroy non persistant database
    """

    admin_data = {
        "first_name": "Admin",
        "last_name": "User",
        "email": "admin@example.com",
        "password": "admin123",
        "is_admin": True
    }
    new_admin = facade.create_user(admin_data)
    print(f"Admin user created with ID: {new_admin.id}")


app = create_app()

if __name__ == '__main__':
    create_admin_user()
    app.run(debug=True)
