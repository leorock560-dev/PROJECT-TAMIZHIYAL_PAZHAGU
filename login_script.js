const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});

function registerUser(username, email, password) {

    if (username === "" || email === "" || password === "") {
        alert("Please fill in all fields");
        return false;
    }

    else{
      window.location.href = "frontend_index.html";
      alert("Registration successful");
      return true;
    }
}

function logIn(username, password) {
    const ADMIN_USER = "tamil1234";
    const ADMIN_PASS = "1234";

    if (username === ADMIN_USER && password === ADMIN_PASS) {
        window.location.href = "frontend_index.html";
        alert("Admin login successful");
        return true;
    }
    else {
        alert("Invalid credentials");
        return false;
    }
}
