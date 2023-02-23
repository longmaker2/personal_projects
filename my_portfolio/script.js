// Get the form element
const form = document.getElementById("contact-form");

// Add an event listener to the form
form.addEventListener("submit", function(event) {
  // Prevent the form from submitting
  event.preventDefault();

  // Get the user's inputs
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const message = document.getElementById("message").value;

  // Create an object to store the form data
  const formData = {
    name: name,
    email: email,
    message: message
  };

  // Send the form data to the server
  fetch("https://example.com/api/contact", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(formData)
  })
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
    // Display a success message to the user
    const formDiv = document.getElementById("contact-form-div");
    const successDiv = document.createElement("div");
    successDiv.innerHTML = "Thank you for contacting us! We'll be in touch soon.";
    formDiv.parentNode.replaceChild(successDiv, formDiv);
  })
  .catch(function(error) {
    // Display an error message to the user
    const formDiv = document.getElementById("contact-form-div");
    const errorDiv = document.createElement("div");
    errorDiv.innerHTML = "There was an error submitting the form. Please try again.";
    formDiv.parentNode.replaceChild(errorDiv, formDiv);
  });
});
