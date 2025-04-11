/**
 * Listen for form submit and send login data to backend
 * Triggered when login button is clicked
 */
document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("login-form");

  if (loginForm) {
    loginForm.addEventListener("submit", async (event) => {
      event.preventDefault();
      let form_email = document.getElementById("email").value;
      let form_password = document.getElementById("password").value;

      loginUser(form_email, form_password);
    });
  }
});

/**
 * Sends login credential to the backend and handle the response
 * If successful : stores the token in a cookie and redirect to home page
 *
 * @param {string} email - User's email address
 * @param {string} password - User's password
 */
async function loginUser(email, password) {
  const response = await fetch("http://127.0.0.1:5000/api/v1/auth/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email, password }),
  });

  if (response.ok) {
    const data = await response.json();
    document.cookie = `token=${data.access_token}; path=/`;
    window.location.href = "index.html";
  } else {
    alert("Login failed: " + response.statusText);
  }
}

/**
 * Run the following function on certains pages load/reload
 */
window.onload = () => {
  // Check login visibility on all pages
  loginVisibility();

  const currentPage = window.location.pathname;

  // If its index, show places list
  if (currentPage.endsWith("index.html") || currentPage === "/") {
    const token = getCookie("token");
    fetchPlaces(token);
  }

  // If it's place.html page, check if user is authenticated and show place details and review
  if (currentPage.endsWith("place.html")) {
    checkAuthentication();
  }
};

/**
 * Hide/show login button depending if the user is logged or not
 * By checking if the cookie with JWT token is present
 */
function loginVisibility() {
  const token = getCookie("token");
  const loginLink = document.getElementById("login-link");

  console.log("Check Cookie...");

  if (loginLink) {
    if (token) {
      console.log("Token found :) => Hide login button");
      loginLink.style.display = "none";
    } else {
      console.log("Token not found :( => Display login button");
      loginLink.style.display = "";
    }
  }
}

/**
 * Check if specific cookie is present and return true or false
 *
 * @param {string} name - Cookie's name
 */
function checkCookie(name) {
  const regex = new RegExp(`(^| )${name}=([^;]+)`);
  const match = document.cookie.match(regex);
  if (match) {
    return true;
  } else {
    return false;
  }
}

/**
 * Get value of a specific cookie and return this value
 *
 * @param {string} name - Cookie's name
 */
function getCookie(name) {
  const regex = new RegExp(`(^| )${name}=([^;]+)`);
  const match = document.cookie.match(regex);
  if (match) {
    return match[2];
  } else {
    return null;
  }
}

/**
 * Fetches places from the backend and displays them on the page
 * Also extracts all prices and stores them for use in the max price filter
 */
async function fetchPlaces(token) {
  // Send GET request to API
  const response = await fetch("http://127.0.0.1:5000/api/v1/places/", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
  });

  if (response.ok) {
    const data = await response.json();
    const placesList = document.querySelector("#places-list ul");

    // Empty existing list (if any)
    placesList.innerHTML = "";

    // Create an empty set to store price of each place (unique)
    let priceSet = new Set();

    data.forEach((place) => {
      const li = document.createElement("li");

      li.innerHTML = `
    <article class="place-card">
        <h3>${place.title}</h3>
        <p>Price per night: <span class="price">${place.price}</span> €</p>
        <div class="details-button">
          <a href="place.html?id=${place.id}">View Details</a>
        </div>
    </article>
  `;

      placesList.appendChild(li);
      priceSet.add(place.price);
    });

    // Filter price
    const sortedPrices = [...priceSet].sort((a, b) => a - b);
    console.log(
      "Prices are found :) and here is the list sorted:",
      sortedPrices
    );

    // Populate price list
    const select = document.getElementById("price-filter");

    // Clean list (if any) and write default value
    select.innerHTML = '<option value="">All</option>';

    sortedPrices.forEach((price) => {
      const option = document.createElement("option");
      option.value = price;
      option.textContent = price + " €";
      select.appendChild(option);
    });
  } else {
    alert("Fetch places failed: " + response.statusText);
  }
}

/**
 * Listens selection in the price filter selector (if is found on page)
 * Filters place cards by price without reloading the page
 */
const priceFilter = document.getElementById("price-filter");

if (priceFilter) {
  priceFilter.addEventListener("change", () => {
    const selectedPrice = parseFloat(priceFilter.value);
    const placeCards = document.querySelectorAll(".place-card");

    placeCards.forEach((card) => {
      const price = parseFloat(card.querySelector(".price").textContent);
      if (price <= selectedPrice || isNaN(selectedPrice)) {
        card.style.display = "";
      } else {
        card.style.display = "none";
      }
    });
  });
}

/**
 * Get place id from URL
 * Catch and return the ID of the place from url ie: place.html?id=f9ab90f
 */
function getPlaceIdFromURL() {
  const placeId = new URLSearchParams(window.location.search);
  return placeId.get("id");
}

/**
 * Check if the user is authenticated
 * If not, hide the add review section
 */
function checkAuthentication() {
  const token = getCookie("token");
  const placeId = getPlaceIdFromURL();
  const addReviewSection = document.getElementById('add-review');

  if (!token) {
    addReviewSection.style.display = "none";
  } else {
    addReviewSection.style.display = "block";
  }

  fetchPlaceDetails(token, placeId);
  fetchReviewsForPlace(placeId);
}

/**
 * Fetches place details from the backend and displays them on the page
 */
async function fetchPlaceDetails(token, placeId) {
  // Send GET request to API
  console.log("API call launched for a specific place...");
  const response = await fetch(
    `http://127.0.0.1:5000/api/v1/places/${placeId}`,
    {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
    }
  );

  if (response.ok) {
    const data = await response.json();
    console.log("Place detail fetched successfully ! :)");

    // update title
    const placeInfo = document.querySelector(".place-info");
    placeInfo.querySelector("h3").textContent = data.title;

    // update details
    document.getElementById(
      "place-owner"
    ).textContent = `${data.owner.first_name} ${data.owner.last_name}`;
    document.getElementById("place-price").textContent = `${data.price} €`;
    document.getElementById(
      "place-description"
    ).textContent = `${data.description}`;
    document.getElementById(
      "place-amenities"
    ).textContent = `To be updated (feature not yet implemented)`;
  } else {
    alert("Fetch place details failed: " + response.statusText);
  }
}

/**
 * Listen for form submit and send review data to backend
 * Triggered when review form is submitted
 */
document.addEventListener('DOMContentLoaded', () => {
  const reviewForm = document.getElementById('review-form');
  const token = getCookie("token");
  const placeId = getPlaceIdFromURL();
  let userId = null;

  // if a token exist, try to decode JWT and found the user ID
  if (token) {
    const base64 = token.split('.')[1];
    const json = atob(base64);
    const decodedToken = JSON.parse(json);
    userId = decodedToken.sub.id;
    console.log("User ID:", userId);
  }

  // send review
  reviewForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const reviewText = document.getElementById('review-text').value;

    const response = await fetch(`http://127.0.0.1:5000/api/v1/reviews/`, {
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
      },
      body: JSON.stringify({
        text: reviewText,
        rating: 5, // temporary, not implemented yet in the form
        user_id: userId,
        place_id: placeId
      })
    });
    if (response.ok) {
      alert("Review submitted!");
      reviewForm.reset();
      location.reload();
    } else {
      alert("Failed to submit review!");
    }
  });
});

/**
 * Fetches reviews for a specific place from the backend and displays them on the page
 */
async function fetchReviewsForPlace(placeId) {
  const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}/reviews`);
  if (!response.ok) {
    console.error("Failed to fetch reviews.");
    return;
  }

  const reviews = await response.json();
  const reviewsContainer = document.getElementById("reviews");

  //  Clean actual contents
  reviewsContainer.innerHTML = "<h2>Reviews</h2>";

  if (reviews.length === 0) {
    const emptyMsg = document.createElement("p");
    emptyMsg.textContent = "No reviews yet.";
    reviewsContainer.appendChild(emptyMsg);
    return;
  }

  reviews.forEach(async (review) => {
    const reviewCard = document.createElement("article");
    reviewCard.classList.add("review-card");

    // create a default value if user dont exist anymore
    let reviewerName = "Anonymous user";

    // Fetch user name through userID
    if (review.user_id) {
      const userData = await fetch(`http://127.0.0.1:5000/api/v1/users/${review.user_id}`);
      if (userData.ok) {
        const user = await userData.json();
        reviewerName = `${user.first_name} ${user.last_name}`;
        console.log("Reviewer name found !")
      }
    }

    reviewCard.innerHTML = `
      <h3>${reviewerName}</h3>
      <p>Review: ${review.text}</p>
      <p>Rating: ${review.rating} stars</p>
    `;

    reviewsContainer.appendChild(reviewCard);
  });
}
