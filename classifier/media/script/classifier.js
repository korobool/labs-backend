$(function() {
    $('#proc-form').submit(function() {
        $.ajax({
            data: $(this).serialize(),
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            success: function(response) {
                $('#genre-field').val(response);
            }
        });
        return false;
    });
});