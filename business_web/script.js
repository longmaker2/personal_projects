// Select all the "Enroll Now" buttons on the page
var enrollButtons = document.querySelectorAll('.button');

// Add a click event listener to each button
enrollButtons.forEach(function(button) {
	button.addEventListener('click', function() {
		alert('Thank you for enrolling in this course!');
	});
});
