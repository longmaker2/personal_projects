<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "database_name";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Prepare statement and bind parameters
$stmt = $conn->prepare("INSERT INTO patients (name, age, gender, medical_history) VALUES (?, ?, ?, ?)");
$stmt->bind_param("siss", $name, $age, $gender, $medical_history);

// Get form data
$name = $_POST["name"];
$age = $_POST["age"];
$gender = $_POST["gender"];
$medical_history = $_POST["medical-history"];

// Execute statement
if ($stmt->execute()) {
  echo "Patient record added successfully";
} else {
  echo "Error adding patient record: " . $conn->error;
}

// Close statement and connection
$stmt->close();
$conn->close();
?>
