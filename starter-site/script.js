// Bluebird Bookkeeping — small site behaviors.
// Only two jobs: the mobile menu, and keeping the footer year current.

document.addEventListener('DOMContentLoaded', function () {

  // Mobile navigation toggle
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.site-nav');

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.innerHTML = open ? '&#10005;' : '&#9776;';
    });
  }

  // Current year in the footer
  var year = document.getElementById('year');
  if (year) {
    year.textContent = new Date().getFullYear();
  }
});
