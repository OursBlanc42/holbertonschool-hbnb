# HBNB Part 4 : Auth & API

## Version 1.0.0

## Disclaimer
For more information about this project, please refer to these README :
- [Main README](https://github.com/OursBlanc42/holbertonschool-hbnb/blob/main/README.md)
- [Part 1 README](https://github.com/OursBlanc42/holbertonschool-hbnb/tree/main/part1/README.md)
- [Part 2 README](https://github.com/OursBlanc42/holbertonschool-hbnb/tree/main/part2/hbnb/README.md)
- [Part 3 README](https://github.com/OursBlanc42/holbertonschool-hbnb/tree/main/part3/README.md)

---

## Table of Contents

- [Intro](#intro)
- [Explanation](#explanation)
  - [HTML](#html)
  - [CSS](#css)
  - [Security, Scalability & Improvements](#security-scalability--improvements)
  - [JS (Frontend)](#js-frontend)
    - [`window.onload`](#windowonload)
    - [`loginUser(email, password)`](#loginuseremail-password)
    - [`loginVisibility()`](#loginvisibility)
    - [`checkAuthentication()`](#checkauthentication)
    - [`checkCookie(name)`](#checkcookiename)
    - [`getCookie(name)`](#getcookiename)
    - [`fetchPlaces(token)`](#fetchplacestoken)
    - [`priceFilter()`](#pricefilter)
    - [`getPlaceIdFromURL()`](#getplaceidfromurl)
    - [`fetchPlaceDetails(token, placeId)`](#fetchplacedetailstoken-placeid)
    - [Review form submit](#review-form-submit)
    - [`fetchReviewsForPlace(placeId)`](#fetchreviewsforplaceplaceid)
- [Getting started](#getting-started)
  - [Prerequisite](#prerequisite)
  - [Installation](#installation)
- [Testing](#testing)
- [Script](#script)
- [Demo Data](#demo-data)
  - [Users](#users)

---


## Intro  
After setting up the project structure in Part 1, implementing the business logic and RESTful API endpoints in Part 2, and enhancing the backend with authentication and database integration in Part 3, we now arrive at the final stage — Part 4.

Unlike the previous parts, this section was completed individually, giving us more creative freedom, especially in designing a visually appealing frontend.

For this reason, I decided to rebrand the project from **HBnB** to **Airbnbear**, giving it a fresh and personal touch.

---

### Explanation

#### HTML
The HTML file was provided as part of the exercise.
I made some slight adjustments to improve the design and layout.

It could still be improved — for example, by adding a "Go back" button or other interactive elements.

#### CSS
The CSS file was also provided.
I tweaked it a bit to enhance the design and added a few fun features, such as animated hover effects.

While it works, there’s definitely room for improvement in terms of responsiveness and structure.

#### Security, Scalability & Improvements
This project is a demo intended to showcase my skills. However, I’m aware that there are several limitations and areas for improvement:

- CORS is currently open to all origins, which isn’t secure for production.
- The app doesn’t use a proper frontend web server.
- Some features are missing (e.g., adding a rating in reviews, showing amenities, allowing users to create places).
- Flask is running with the built-in development server, which isn’t suitable for production.
- No real automated testing has been implemented — only manual/visual tests.
- Divide the script.js file in several file and more DRY
- And probably a few other things I forgot...

This project is a solid foundation but not production-ready — and that’s okay. It’s all part of the learning process.

#### JS (Frontend)

This file manages the frontend interactions for the Airbnbear project.  
It handles login, place listing, place details, user authentication, review submission, and filtering.



##### `window.onload`
Triggered on each page load/reload:
- On all pages: calls `loginVisibility()` to show or hide the login button depending on the presence of a token (i.e. user is logged in or not)
- On `index.html`: calls `fetchPlaces()` to display all available places
- On `place.html`: calls `checkAuthentication()` to show or hide the review section based on the user's login status. It also fetches place details in any case



##### `loginUser(email, password)`
- Triggered by an event listener on the login form
- Sends login credentials to the backend API
- On success: stores the token in a cookie and redirects to the homepage
- On failure: displays `Login failed` with the response status



##### `loginVisibility()`
- Shows or hides the login link depending on whether the user is logged in (based on token presence)



##### `checkAuthentication()`
- Hides the review section if the user is not authenticated
- Fetches and displays place details and associated reviews



##### `checkCookie(name)`
- Returns `true` if a specific cookie is present, otherwise `false`


##### `getCookie(name)`
- Returns the value of a specified cookie, or `null` if not found



##### `fetchPlaces(token)`
- Sends a `GET` request to fetch all places from the backend
- On success:
  - Creates a DOM block for each place
  - Collects and deduplicates prices
  - Sorts prices and populates the price filter
- On failure: shows `Fetch places failed` with the status message



##### `priceFilter()`
- Event listener triggered when the user selects a specific price
- Hides places that exceed the selected price



##### `getPlaceIdFromURL()`
- Retrieves the `id` parameter from the URL (e.g. `place.html?id=f9ab90f`)



##### `checkAuthentication()`
- Extracts the token from cookies
- Retrieves the place ID from the URL
- Displays or hides the review form depending on the token
- Calls `fetchPlaceDetails()` and `fetchReviewsForPlace()`



##### `fetchPlaceDetails(token, placeId)`
- Sends a `GET` request to fetch details about a specific place
- On success: updates the DOM with title, price, description, etc.
- On failure: displays an error



##### Review form submit
- Event listener on the review form submission
- If a token exists: decodes the JWT to extract the user ID
- Sends the review to the API via `POST`
  - Currently, the rating is always `5 stars` (rating selector not implemented yet)
- On success: shows `Review submitted!`
- On failure: shows `Failed to submit review!`



##### `fetchReviewsForPlace(placeId)`
- Fetches all reviews linked to a given place
- If no reviews are found: shows `No reviews yet.`
- If a user doesn't exist anymore: displays `Anonymous user`
- Fetches the reviewer's name from the API using `user_id`
- Updates the DOM with reviewer name, review text, and rating (default: 5 stars)


---

## Getting started
**Disclaimer : These explanations was tested on my Linux machine. So it's valid on a Linux system only.**

### Prerequisite
- `Linux system` (tested on Linux Mint 22.1 x86_64 with 6.8.0-52-generic kernel )
- `Python3` (version 3.12.3)
- `venv`
- `browser` (tested on Firefox 136.0.4 and GNOME Web 46.0)
Additional :
- `Postman` (for testing only)
- Somes SQL tools if you want to manipulate database

### Installation
1. Clone / download the repository
`git clone https://github.com/OursBlanc42/holbertonschool-hbnb`

2. Go to the right directory
`cd holbertonschool-hbnb/part4/hbnb`

3. Setup a virtual environnement 
`python3 -m venv venv`

4. Activate virtual env
`source venv/bin/activate`

5. Install the Python packages needed for the project. There are listed in requirements.txt as explained before.
`pip install -r requirements.txt`

6. From this virtual environnement you can now run the script (more detail below)
`./setup.sh`

7. If everything has gone well, the terminal should display something like : 
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
Admin user already exists. Check the README for default credentials.
 * Debugger is active!
 * Debugger PIN: 112-991-365

```

8. Now, you can open the `part4/index.html` in your favorite browser !

9. Optionnal : You can also try the API with cURL, Postman, Swagger web UI, or whatever... You can find more information about this in part 3 of the project.

---

### Testing  
For this part of the project, most of the testing was done visually by navigating the website and trying various usage scenarios.  
I also performed some tests using a Postman collection, which you can find in the `hbnb/tests` directory.

**Note:** Some of these tests fail (especially edge cases or unusual scenarios), likely due to inconsistencies between the backend and the database that still need to be fixed.

---

### Script  
To simplify setup, I created a Bash script that performs the following steps:
- Creates the database
- Creates all required tables
- Populates the database with demo data
- Starts the backend server

---

### Demo Data  
The SQL file used to populate the demo database creates:
- Three users
- Several places
- Reviews
- Some amenities (**note:** amenities are not yet implemented on the frontend)


#### Users
As mentioned earlier, three users have been created for testing purposes.
You can use the following credentials to log in:

##### John Doe  
- **Email:** `john@example.com`
- **Password:** `azerty123`
- **Role:** Regular user (not admin)

##### Jane Doe  
- **Email:** `jane@example.com`
- **Password:** `azerty123`
- **Role:** Regular user (not admin)

##### Admin  
- **Email:** `admin@example.com`
- **Password:** `admin123`
- **Role:** Administrator



