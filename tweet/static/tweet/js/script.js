// Toggle mobile menu
const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');

menuToggle.addEventListener('click', () => {
  navLinks.classList.toggle('active');
});

// Mobile menu
const menuToggle = document.getElementById('menuToggle');
const navLinks = document.getElementById('navLinks');

menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
    menuToggle.classList.toggle('active');
    const expanded = menuToggle.getAttribute('aria-expanded') === 'true';
    menuToggle.setAttribute('aria-expanded', !expanded);
});

// Close mobile menu when clicking link
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('active');
        menuToggle.classList.remove('active');
        menuToggle.setAttribute('aria-expanded', 'false');
    });
});

// Sticky navbar shadow
window.addEventListener('scroll', () => {
    const header = document.querySelector('.header');
    if (window.scrollY > 50) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});

// Back to top button
const backToTop = document.getElementById('backToTop');
window.addEventListener('scroll', () => {
    backToTop.style.opacity = window.scrollY > 400 ? '1' : '0';
    backToTop.style.pointerEvents = window.scrollY > 400 ? 'all' : 'none';
});

backToTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

// Simple testimonial slider
const testimonials = document.querySelectorAll('.testimonial');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
let current = 0;

function showTestimonial(index) {
    testimonials.forEach((t, i) => {
        t.classList.remove('active');
        if (i === index) {
            t.classList.add('active');
        }
    });
}

prevBtn.addEventListener('click', () => {
    current = (current - 1 + testimonials.length) % testimonials.length;
    showTestimonial(current);
});

nextBtn.addEventListener('click', () => {
    current = (current + 1) % testimonials.length;
    showTestimonial(current);
});

// Optional: auto slide every 7 seconds
// setInterval(() => {
//     current = (current + 1) % testimonials.length;
//     showTestimonial(current);
// }, 7000);

// Basic form validation & feedback
const form = document.getElementById('contactForm');
form.addEventListener('submit', (e) => {
    e.preventDefault();
    // Here you would normally send data via fetch / axios
    document.getElementById('formMessage').textContent = "Thank you! We'll get back to you soon ☕";
    form.reset();
});




















// Testimonials slider
const testimonials = document.querySelectorAll('.testimonial');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');

let currentTestimonial = 0;

function showTestimonial(index) {
  testimonials.forEach((testi, i) => {
    testi.classList.toggle('active', i === index);
  });
}

prevBtn.addEventListener('click', () => {
  currentTestimonial = (currentTestimonial - 1 + testimonials.length) % testimonials.length;
  showTestimonial(currentTestimonial);
});

nextBtn.addEventListener('click', () => {
  currentTestimonial = (currentTestimonial + 1) % testimonials.length;
  showTestimonial(currentTestimonial);
});

showTestimonial(currentTestimonial);

// Contact form validation and submission
const form = document.getElementById('contactForm');
const formMessage = document.getElementById('formMessage');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  let isValid = true;
  form.querySelectorAll('.error-msg').forEach(el => el.textContent = '');

  const nameField = form.name;
  if (!nameField.value.trim()) {
    setError(nameField, 'Name is required');
    isValid = false;
  }

  const emailField = form.email;
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailField.value.trim()) {
    setError(emailField, 'Email is required');
    isValid = false;
  } else if (!emailPattern.test(emailField.value.trim())) {
    setError(emailField, 'Email is invalid');
    isValid = false;
  }

  const messageField = form.message;
  if (!messageField.value.trim()) {
    setError(messageField, 'Message is required');
    isValid = false;
  }

  if (isValid) {
    formMessage.textContent = 'Sending message...';

    try {
      // Send form data to Django backend
      const response = await fetch('/contact/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json', 'X-CSRFToken': getCookie('csrftoken')},
        body: JSON.stringify({
          name: nameField.value.trim(),
          email: emailField.value.trim(),
          message: messageField.value.trim()
        })
      });

      if (response.ok) {
        formMessage.textContent = 'Thank you! We received your message.';
        form.reset();
      } else {
        formMessage.textContent = 'Something went wrong. Try again.';
      }
    } catch (err) {
      formMessage.textContent = 'Error sending message.';
    }
  }
});

function setError(field, message) {
  const errorEl = field.parentElement.querySelector('.error-msg');
  errorEl.textContent = message;
}

// Helper to get CSRF token for Django
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Order Now button
const orderButtons = document.querySelectorAll('.btn-order');
orderButtons.forEach(button => {
  button.addEventListener('click', async () => {
    const flavor = button.dataset.flavor;

    try {
      const response = await fetch('/order/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json', 'X-CSRFToken': getCookie('csrftoken')},
        body: JSON.stringify({flavor})
      });

      if (response.ok) {
        alert(`Thank you for choosing ${flavor}! Your order is being processed.`);
      } else {
        alert('Failed to place order. Try again.');
      }
    } catch (err) {
      alert('Error placing order.');
    }
  });
});
