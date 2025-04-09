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
 * Run the following function on each page load / reload
 */
window.onload = function () {
  loginVisibility();
  const token = getCookie("token");
  fetchPlaces(token);
};

/**
 * Hide/show login button depending if the user is logged or not
 * By checking if the cookie with JWT token is present
 */
function loginVisibility() {
  let token = checkCookie("token");
  console.log("Check Cookie...");
  if (token == true) {
    console.log("Token found :) => Hide login button");
    document.getElementById("login-link").style.display = "none";
  } else {
    console.log("Token not found :( => Display login button");
    document.getElementById("login-link").style.display = "";
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
 * Get value of a specific cookie and return this alue
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
      "Authorization": `Bearer ${token}`
    },
  });

  if (response.ok) {
    const data = await response.json();
    const placesList = document.querySelector("#places-list ul");

    // Empty existing list (if any)
    placesList.innerHTML = "";

    // Create an empty set to store price of each place (unique)
    let priceSet = new Set();

    data.forEach(place => {
      const li = document.createElement("li");

      li.innerHTML = `
    <article class="place-card">
        <h3>${place.title}</h3>
        <p>Price per night: <span class="price">${place.price}</span> €</p>
        <div class="details-button">
            <p>View Details</p>
        </div>
    </article>
  `;

      placesList.appendChild(li);
      priceSet.add(place.price);
    });

    // Filter price
    const sortedPrices = [...priceSet].sort((a, b) => a - b);
    console.log("Prices are found :) and here is the list sorted:", sortedPrices);

    // Populate price list
    const select = document.getElementById("price-filter");

    // Clean list (if any) and write default value
    select.innerHTML = '<option value="">All</option>';

    sortedPrices.forEach(price => {
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
 * Listens selection in the price filter selector
 * Filters place cards by price without reloading the page
 */
document.getElementById("price-filter").addEventListener("change", () => {
  const selectedPrice = parseFloat(document.getElementById("price-filter").value);
  const placeCards = document.querySelectorAll(".place-card");

  placeCards.forEach(card => {
    const price = parseFloat(card.querySelector(".price").textContent);
    if (price <= selectedPrice || isNaN(selectedPrice)) {
      card.style.display = "";
    } else {
      card.style.display = "none";
    }
  });
});



