// Wait for the document to be fully loaded before running the script
document.addEventListener("DOMContentLoaded", function() {
  // Get the form element
  const form = document.getElementById("patient-form");

  // Add an event listener for the submit event
  form.addEventListener("submit", function(event) {
    // Prevent the form from being submitted normally
    event.preventDefault();

    // Get the form data
    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;
    const gender = document.getElementById("gender").value;
    const medicalHistory = document.getElementById("medical-history").value;

    // Validate the form data
    if (name.trim() === "") {
      alert("Please enter a name");
      return;
    }

    if (age < 0) {
      alert("Please enter a valid age");
      return;
    }

    if (gender === "") {
      alert("Please select a gender");
      return;
    }

    // Create a new AJAX request
    const xhr = new XMLHttpRequest();

    // Set up the request
    xhr.open("POST", "add-patient.php");
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    // Set up the response handler
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        alert(xhr.responseText);
        form.reset();
      }
    };

    // Send the request
    xhr.send(`name=${name}&age=${age}&gender=${gender}&medical-history=${medicalHistory}`);
  });
});
