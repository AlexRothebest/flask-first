function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = cookies[i].trim();
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}


$(document).ready(function() {
	$('.login-form > button').click(function() {
		$(this).find('.fa-spinner').show();
		$(this).css({
			'padding-left': '10px' 
		});


		let usernameField = $("fieldset > input[name='username']"),
			passwordField = $("fieldset > input[name='password']"),

			username = usernameField.val(),
			password = passwordField.val(),

			formIsCorrect = true;


		$('fieldset small.error').remove();

		$('fieldset input').css({
			'border-color': 'black'
		});


		if (username.length == 0) {
			usernameField.css({
				'border-color': 'red'
			}).after("<small class='error'>Username field mustn't be empty</small>");


			formIsCorrect = false;
		}

		if (password.length == 0) {
			passwordField.css({
				'border-color': 'red'
			}).after("<small class='error'>Password field mustn't be empty</small>");


			formIsCorrect = false;
		}


		if (formIsCorrect) {
			$.ajax({
				url: '/api/login/',
				method: 'POST',
				async: true,
				headers: {
					'X-Csrf-Token': getCookie('csrfmiddlewaretoken')
				},
				data: {
					password: password,
					username: username
				},
				success: function(result) {
					if (result.success) {
						location.href = '/'
					} else {
						$(this).before("<small class='error'>Wrong username or password</small>")
					}
				},
				error: function() {
					alert('Error in AJAX');
				}
			});
		}
	});
});