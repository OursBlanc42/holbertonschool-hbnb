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

8. Now, you can enjoy and try the API with CURL, Postman, Swagger web UI, or whatever... See examples below


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

##### Attributes
None

##### Relations
None

##### Specific methods
`save()` : Update the updated_at timestamp whenever the object is modified
`update(data)` : Update the attributes of the object based on the provided dictionary

#### - User class

##### Description
The user class inherit from BaseModel and manage the user informations.

#### Attributes
`id` (String): Unique identifier for each user.
`first_name` (String): The first name of the user. Required, maximum length of 50 characters.
`last_name` (String): The last name of the user. Required, maximum length of 50 characters.
`email` (String): The email address of the user. Required, must be unique, and should follow standard email format validation.
`is_admin` (Boolean): Indicates whether the user has administrative privileges. Defaults to False.
`created_at` (DateTime): Timestamp when the user is created.
`updated_at` (DateTime): Timestamp when the user is last updated.

##### Relations
A **User** can own multiple **Place** instances (one-to-many relationship).
A **User** can have multiple **Review** instances associated (one-to-many relationship).

##### Specific methods
None


#### - Place class
##### Description
The place class inherit from BaseModel and manage the place informations.

##### Attributes
`id` (String): Unique identifier for each place.
`title` (String): The title of the place. Required, maximum length of 100 characters.
`description` (String): Detailed description of the place. Optional.
`price` (Float): The price per night for the place. Must be a positive value.
`latitude` (Float): Latitude coordinate for the place location. Must be within the range of -90.0 to 90.0.
`longitude` (Float): Longitude coordinate for the place location. Must be within the range of -180.0 to 180.0.
`owner` (User): User instance of who owns the place. This should be validated to ensure the owner exists.
`created_at` (DateTime): Timestamp when the place is created.
`updated_at` (DateTime): Timestamp when the place is last updated.


##### Relations
A **Place** can have multiple **Review** instances (one-to-many relationship).
A **Place** can have multiple **Amenity** instances (many-to-many relationship).
A **Place** can have one **Owner** (referencing to **User**) (one-to-one relationship).

##### Specific methods
None








#### - Review class
##### Description
The review class inherit from BaseModel and manage the review informations.

##### Attributes
`id` (String): Unique identifier for each review.
`text` (String): The content of the review. Required.
`rating` (Integer): Rating given to the place, must be between 1 and 5.
`place` (Place): Place instance being reviewed. Must be validated to ensure the place exists.
`user` (User): User instance of who wrote the review. Must be validated to ensure the user exists.
`created_at` (DateTime): Timestamp when the review is created.
`updated_at` (DateTime): Timestamp when the review is last updated.

##### Relations
A **Review** can have one **User** instances (one-to-one relationship)
A **Review** can have one **Place** instances (one-to-one relationship)

##### Specific methods
None




#### - Amenity class
##### Description
The review class inherit from BaseModel and manage the amenities available.

##### Attributes

`id` (String): Unique identifier for each amenity.
`name` (String): The name of the amenity (e.g., "Wi-Fi", "Parking"). Required, maximum length of 50 characters.
`created_at` (DateTime): Timestamp when the amenity is created.
`updated_at` (DateTime): Timestamp when the amenity is last updated.

##### Relations
A **Amenity** can exist in multiple **Place** instances.


##### Specific methods
None




### Core Classes and Methods
#### - HBnBFacade (Main entry point)
The Facade architecture centralizes communication between client and business layer.

#### - Repository (Managing users)
At this point of the project, we will manage data persistance with in-memory repository. This repository will later be replaced by a database-backed solution in Part 3.

We using the following repository to store associated data
- UserRepository
- AmenityRepository
- PlaceRepository
- ReviewRepository

### Usage Examples
#### - Creating a User
#### - Retrieving a User
#### - Updating a User
#### - Creating an Amenity
#### - Listing All Amenities




