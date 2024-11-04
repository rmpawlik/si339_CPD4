// Select all images on the page
document.querySelectorAll('img').forEach(img => {
    img.onerror = function() {
      this.onerror = null; // Prevents infinite loop if default image missing
      this.src = '../images/default_image.jpg';
      this.alt = ""
    };
  });
//   confused how this is being called becuase it is not relying on any event listener??



// // Select all images on the page
// document.querySelectorAll('img').forEach(img => {
//     const imgSrc = img.src;
  
//     // Create a new Image object to check if the image source exists
//     const testImg = new Image();
//     testImg.onload = function() {
//       img.src = imgSrc; // Original image loaded successfully
//     };
//     testImg.onerror = function() {
//       img.src = '../images/default_image.jpg'; // Use default image if original not found
//       img.alt = ""; // Clear alt if needed
//     };
  
//     // Attempt to load the original image
//     testImg.src = imgSrc;
//   });