document.addEventListener('DOMContentLoaded', function() {
  // Get all navigation links
  const navLinks = document.querySelectorAll('nav a');
  
  // Get current path and normalize it (remove trailing slash if it exists)
  let currentPath = window.location.pathname;
  if (currentPath.endsWith('/') && currentPath !== '/') {
    currentPath = currentPath.slice(0, -1);  // Remove trailing slash
  }
  
  console.log("Normalized current path:", currentPath);
  
  // Loop through all nav links
  navLinks.forEach(link => {
    let href = link.getAttribute('href');
    // Normalize href too (remove trailing slash if it exists)
    if (href.endsWith('/') && href !== '/') {
      href = href.slice(0, -1);
    }
    
    console.log("Checking if", href, "matches", currentPath);
    
    // Apply current-page class if the href matches the current path
    if (href === currentPath) {
      console.log("Match found! Adding current-page class to", href);
      link.classList.add('current-page');
    }
  });
});