$(document).ready(function() {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie('csrftoken');

    $("#searchbar").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "{% url 'autocomplete' %}",
                dataType: "json",
                data: {
                    term: request.term
                },
                headers: {
                    "X-CSRFToken": csrftoken
                },
                success: function(data) {
                    response(data);
                },
                error: function(xhr, status, error) {
                    console.error("Error:", error);
                    response([]);
                }
            });
        },
        minLength: 2
    });
});

$("#searchbar").autocomplete({
    source: ["Test1", "Test2", "Test3"],
    minLength: 2
});