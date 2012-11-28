$(function() {
	$('#send-btn').click(function() {
		$('#genre-field').val("Detecting genre...");
	});
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
	$('.close').click(function() {
		$(this).parent().toggle();
	});
});