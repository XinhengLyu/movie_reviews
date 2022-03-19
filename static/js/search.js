$(document).ready(function () {

    $('#search-input').keyup(function () {
        var query;
        query = $(this).val();
        $.get('/movie/movie_suggestions/', {'suggestion': query}, function (data) {
            $('#movie-listing').html(data);
        });
    });
});