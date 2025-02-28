# HBNB Part 2 - BL and API

## Disclaimer
For more information about this project, please refer to Part 1 README.md

## Intro
After creating the project structure using the various diagrams in part 1, the aim of this part 2 is to :
- Set up the structure
- Implement the business logic layer
- Create endpoints for the RESTful API
- Test and validate the API

## Project structure
The project is organized with this structure :
```
hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   ├── persistence/
│       ├── __init__.py
│       ├── repository.py
├── run.py
├── config.py
├── requirements.txt
├── README.md

```

### Explanation

- The `app/` directory contains the core application code.
- The `api/ `subdirectory houses the API endpoints, organized by version (v1/).
- The `models/` subdirectory contains the business logic classes (e.g., user.py, place.py).
- The `services/ `subdirectory is where the Facade pattern is implemented, managing the interaction between layers.
- The `persistence/` subdirectory is where the in-memory repository is implemented. This will later be replaced by a database-backed solution using SQL Alchemy.
- `run.py` is the entry point for running the Flask application.
- `config.py` will be used for configuring environment variables and application settings.
- `requirements.txt` will list all the Python packages needed for the project. 
- `README.md` (The present document) will contain a brief overview of the project.


### Further information
As explain in the introduction, we have made some tests to validate our API. 
This tests can be found in the branch *develop* of this project in the `hbnb/tests` directory.


## Getting started
**Disclaimer : These explanations are valid on a Linux system only.**

### Prerequisite
- `Linux system` (tested on Linux Mint 22.1 x86_64 with 6.8.0-52-generic kernel )
- `Python3` (version 3.12.3)
- `venv`

### Installation
1. Clone / download the repository
`git clone https://github.com/OursBlanc42/holbertonschool-hbnb`

2. Go to the right directory
`cd holbertonschool-hbnb/part2/hbnb`

3. Setup a virtual environnement 
`python3 -m venv venv`

4. Activate virtual env
`source venv/bin/activate`

5. Install the Python packages needed for the project. There are listed in requirements.txt as explained before.
`pip install -r requirements.txt`

6. From this virtual environnement you can now run the application
`python run.py`

7. If everything has gone well, the terminal should display
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 781-035-494
```

8. Now, you can enjoy and try the API with cURL, Postman, Swagger web UI, or whatever... See examples below


## Business Logic Layer Explanation

### Overview

The Business Logic Layer contains the core business logic and the models that represent the entities in the system. The main ones being Users; Amenities; Places; and Reviews.

### Entities and Their Responsibilities



#### BaseModel class

##### Description

As this project uses OOP concepts, the main classes (Users, Amenities, Place, and Reviews) will inherit from a parent class called `BaseModel`, which will assign a unique identifier (UUID) to each instance, and for auditing purposes, a creation date and an update date.

Each time an object (Users, Amenities, Review, Place) is created, a unique UUID will be created with a creation date. And each time the object is updated, the update date will be updated.

As this behaviour is the same for all objects, it has been implemented in this parent class so that each child 
inherits these behaviours.

##### Specific methods
`save()` : Update the updated_at timestamp whenever the object is modified
`update(data)` : Update the attributes of the object based on the provided dictionary



#### - User class

##### Description
The user class inherit from BaseModel and manage the user informations.

#### Attributes
| Attribute    | Type      | Description                                              |
|-------------|----------|----------------------------------------------------------|
| `id`        | String   | Unique identifier for each user                          |
| `first_name` | String   | The first name of the user (Required, max 50 chars)     |
| `last_name`  | String   | The last name of the user (Required, max 50 chars)      |
| `email`      | String   | Unique email address (Required, must follow email format) |
| `is_admin`   | Boolean  | Indicates if user has admin privileges (Defaults to False) |
| `created_at` | DateTime | Timestamp when the user is created                      |
| `updated_at` | DateTime | Timestamp when the user is last updated                 |

##### Relations
A **User** can own multiple **Place** instances (one-to-many relationship).
A **User** can have multiple **Review** instances associated (one-to-many relationship).



#### - Place class

##### Description
The place class inherit from BaseModel and manage the place informations.

##### Attributes
| Attribute    | Type      | Description                                                    |
|-------------|----------|----------------------------------------------------------------|
| `id`        | String   | Unique identifier for each place                              |
| `title`     | String   | The title of the place (Required, max 100 chars)              |
| `description` | String  | Detailed description of the place (Optional)                 |
| `price`     | Float    | Price per night (Must be a positive value)                    |
| `latitude`  | Float    | Latitude coordinate (-90.0 to 90.0)                           |
| `longitude` | Float    | Longitude coordinate (-180.0 to 180.0)                        |
| `owner`     | User     | User instance who owns the place (Validated to ensure it exists) |
| `created_at` | DateTime | Timestamp when the place is created                          |
| `updated_at` | DateTime | Timestamp when the place is last updated                     |

##### Relations
A **Place** can have multiple **Review** instances (one-to-many relationship).
A **Place** can have multiple **Amenity** instances (many-to-many relationship).
A **Place** can have one **Owner** (referencing to **User**) (many-to-one relationship).



#### - Review class

##### Description
The review class inherit from BaseModel and manage the review informations.

##### Attributes
| Attribute    | Type      | Description                                                   |
|-------------|----------|---------------------------------------------------------------|
| `id`        | String   | Unique identifier for each review                            |
| `text`      | String   | The content of the review (Required)                         |
| `rating`    | Integer  | Rating given to the place (Must be between 1 and 5)          |
| `place`     | Place    | Place instance being reviewed (Validated to ensure it exists) |
| `user`      | User     | User instance who wrote the review (Validated to ensure it exists) |
| `created_at` | DateTime | Timestamp when the review is created                        |
| `updated_at` | DateTime | Timestamp when the review is last updated                   |

##### Relations
A **Review** is linked to one **User** instances (many-to-one relationship)
A **Review** can have one **Place** instances (one-to-one relationship)



#### - Amenity class

##### Description
The review class inherit from BaseModel and manage the amenities available.

##### Attributes

| Attribute    | Type      | Description                                                   |
|-------------|----------|---------------------------------------------------------------|
| `id`        | String   | Unique identifier for each amenity                           |
| `name`      | String   | The name of the amenity (e.g., "Wi-Fi", "Parking") (Required, max 50 chars) |
| `created_at` | DateTime | Timestamp when the amenity is created                        |
| `updated_at` | DateTime | Timestamp when the amenity is last updated                   |

##### Relations
A **Amenity** can exist in multiple **Place** instances.

##### Specific methods
None



### Core Classes and Methods
#### - HBnBFacade (Main entry point)
The Facade architecture centralizes communication between client and business layer.

##### Methods

| Method                            | Description                                   |
|-----------------------------------|-----------------------------------------------|
| **User Methods**                  |
| `create_user(user_data)`          | Creates a new user with the provided data     |
| `get_all_users()`                 | Retrieves all users                           |
| `get_user(user_id)`               | Retrieves a user by their unique ID           |
| `get_user_by_email(email)`        | Finds a user using their email address        |
| `update_user(user_id, user_data)` | Updates an existing user by ID                | 
| **Amenity Methods**               |
| `create_amenity(amenity_data)`    | Creates a new amenity                         |
| `get_amenity(amenity_id)`         | Retrieves an amenity by ID                    |
| `get_all_amenities()`             | Retrieves all amenities                       |
| `update_amenity(amenity_id, amenity_data)` | Updates an existing amenity by ID    |
| **Place Methods**                 |
| `create_place(place_data)`        | Creates a new place                           |
| `get_place(place_id)`             | Retrieves a place by ID                       |
| `get_all_places()`                | Retrieves all places                          |
| `update_place(place_id, place_data)` | Updates an existing place by ID            |
| **Review Methods**                |
| `create_review(review_data)`      | Creates a new review for a place              |
| `get_review(review_id)`           | Retrieves a review by ID                      |
| `get_all_reviews()`               | Retrieves all reviews                         |
| `get_reviews_by_place(place_id)`  | Retrieves all reviews for a specific place    |
| `update_review(review_id, review_data)` | Updates an existing review by ID        |
| `delete_review(review_id)`        | Deletes a review by ID                        |



#### - Repository (Managing users)
At this point of the project, we will manage data persistance with in-memory repository. This repository will later be replaced by a database-backed solution in Part 3.

We using the following repository to store associated data
- UserRepository
- AmenityRepository
- PlaceRepository
- ReviewRepository

### Usage Examples
Find below some examples with cURL (you can also use software like Postman or use the web user interface SwaggerUI)
The server is considered to be running

#### - Creating a User
##### Input
```bash
curl -X POST http://127.0.0.1:5000/api/v1/users/ \
     -H "Content-Type: application/json" \
     -d '{
           "first_name": "John",
           "last_name": "Doe",
           "email": "john.doe@example.com"
         }'
```
##### Output
```bash
{
    "id": "3f6a434a-42af-4634-a7c6-b945a07f600c",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com"
}
```

#### - Creating an Amenity
##### Input
```bash
curl -X POST http://127.0.0.1:5000/api/v1/amenities/ \
     -H "Content-Type: application/json" \
     -d '{
           "name": "Wi-Fi"
         }'
```
##### Output
```bash
{
    "id": "04f718f4-d1f9-4495-96b3-8622bf28d42b",
    "name": "Wi-Fi"
}
```

#### - Listing All Amenities
In the same way as seen above, we've created other amenities to make the example more meaningful.

##### Input
```bash
curl -X GET http://127.0.0.1:5000/api/v1/amenities/
```

##### Output
```bash
[
    {
        "id": "04f718f4-d1f9-4495-96b3-8622bf28d42b",
        "name": "Wi-Fi"
    },
    {
        "id": "321942bc-bc40-44f5-bd21-4d0d6b697ae6",
        "name": "Ping-pong table"
    },
    {
        "id": "1e04ac41-4a51-4508-860c-f158f4432ccd",
        "name": "Sauna"
    }
]
```

#### - Create a place

#### - Edit a place

#### - Add a review

#### - Delete a review



