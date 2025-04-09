/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
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

async function loginUser(email, password) {
  const response = await fetch("http://127.0.0.1:5000/api/v1/auth/login/", {
    method: "POST",
    credentials: 'include',
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

window.onload = function () {
  loginVisibility();
  fetchPlaces();
};

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

function checkCookie(name) {
  const regex = new RegExp(`(^| )${name}=([^;]+)`);
  const match = document.cookie.match(regex);
  if (match) {
    return true;
  } else {
    return false;
  }
}

async function fetchPlaces() {
    const response = await fetch("http://127.0.0.1:5000/api/v1/places/", {
      method: "GET",
      credentials: 'include',
      headers: {
        "Content-Type": "application/json",
        credentials: "include",
      },
    });

    if (response.ok) {
      const data = await response.json();
      console.log(data);
    } else {
      alert("Fetch places failed: " + response.statusText);
    }
  }
