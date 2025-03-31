// navigation.js
document.addEventListener('DOMContentLoaded', function() {
    // Get current path
    const path = window.location.pathname;
    
    // Your actual basepath - should match what you're using in build.sh
    const basePathPrefix = "/Static-Site-Generator"; 
    
    // Remove the basepath from the current path for comparison
    const relativePath = path.startsWith(basePathPrefix) 
      ? path.substring(basePathPrefix.length) || '/' 
      : path;
    
    // Find all navigation links
    const navLinks = document.querySelectorAll('nav a');
    
    // Check each link to see if it matches the current path
    navLinks.forEach(link => {
      // Get the href attribute
      const href = link.getAttribute('href');
      
      // Remove the basepath from the href for comparison
      const relativeHref = href.startsWith(basePathPrefix) 
        ? href.substring(basePathPrefix.length) || '/' 
        : href;
      
      // If this link matches the current path, add the 'current-page' class
      if(relativeHref === relativePath) {
        link.classList.add('current-page');
      }
    });
  });