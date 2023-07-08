// Wait for the document to load before running the code
$(document).ready(function() {

  // Add a click event listener to the submit button
  $('button[type="submit"]').click(function(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    // Get the form data and send it to the server
    var formData = $('form').serialize();
    $.ajax({
      type: 'POST',
      url: '/reset-password/',
      data: formData,
      success: function(response) {
        // Show a success message
        alert('Your password has been reset successfully!');
      },
      error: function(xhr) {
        // Show an error message
        alert('An error occurred while resetting your password. Please try again later.');
      }
    });
  });

});
// custom script for confirm password reset page
console.log('Confirm password reset page loaded');
