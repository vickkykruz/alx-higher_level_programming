$(document).ready(function() {
      // Fetch translation data from the provided URL
    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        method: 'GET',
        dataType: 'json',
        success: function(data) {
          // Display the translation in DIV#hello
            $('#hello').text(data.hello);
        },
        error: function() {
            console.error('Failed to fetch translation data.');
        }
    });
})
