// Fetch character data from the provided URL
$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function(data) {
        // Extract and display the character name in DIV#character
        $('#character').text(data.name);
    },
    error: function() {
        console.error('Failed to fetch character data.');
    }
});
