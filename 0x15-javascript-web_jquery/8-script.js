// Fetch movie data from the provided URL
$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function(data) {
        // Iterate through each movie and append its title to UL#list_movies
        $.each(data.results, function(index, movie) {
            $('#list_movies').append('<li>' + movie.title + '</li>');
        });
    },
    error: function() {
        console.error('Failed to fetch movie data.');
    }
});
