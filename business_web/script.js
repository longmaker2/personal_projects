// Navigation toggle
const menuToggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('nav');

menuToggle.addEventListener('click', () => {
  nav.classList.toggle('active');
});

// Scroll to top button
const scrollToTopBtn = document.querySelector('.scroll-to-top');

window.addEventListener('scroll', () => {
  if (window.pageYOffset > 100) {
    scrollToTopBtn.classList.add('show');
  } else {
    scrollToTopBtn.classList.remove('show');
  }
});

scrollToTopBtn.addEventListener('click', () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
});

// Form validation
const form = document.querySelector('form');
const nameInput = document.querySelector('#name');
const emailInput = document.querySelector('#email');
const messageInput = document.querySelector('#message');

form.addEventListener('submit', (e) => {
  e.preventDefault();

  // Check for name input
  if (nameInput.value === '') {
    setErrorFor(nameInput, 'Name is required');
  } else {
    setSuccessFor(nameInput);
  }

  // Check for email input
  if (emailInput.value === '') {
    setErrorFor(emailInput, 'Email is required');
  } else if (!isValidEmail(emailInput.value)) {
    setErrorFor(emailInput, 'Email is not valid');
  } else {
    setSuccessFor(emailInput);
  }

  // Check for message input
  if (messageInput.value === '') {
    setErrorFor(messageInput, 'Message is required');
  } else {
    setSuccessFor(messageInput);
  }
});

function setErrorFor(input, message) {
  const formControl = input.parentElement;
  const error = formControl.querySelector('.error-message');
  formControl.classList.add('error');
  error.innerText = message;
}

function setSuccessFor(input) {
  const formControl = input.parentElement;
  formControl.classList.remove('error');
}

function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}
