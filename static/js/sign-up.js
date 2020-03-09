$(document).ready(function() {
	$('fieldset > label.submit-btn').click(function() {
		let usernameField = $("fieldset > input[name='username']"),
			emailField = $("fieldset > input[name='email']"),
			passwordField = $("fieldset > input[name='password']"),
			confirmPasswordField = $("fieldset > input[name='confirm-password']"),

			password = passwordField.val(),
			confirmPassword = confirmPasswordField.val(),

			formIsCorrect = true;


		$('fieldset small.error').remove();

		$('fieldset input').css({
			'border-color': 'black'
		});


		if (usernameField.val().length == 0) {
			usernameField.css({
				'border-color': 'red'
			}).after("<small class='error'>Username is required</small>");


			formIsCorrect = false;
		} else if (usernameField.val().length < 2) {
			usernameField.css({
				'border-color': 'red'
			}).after("<small class='error'>Username must be at least 2 characters</small>");


			formIsCorrect = false;
		}


		if (emailField.val().length == 0) {
			emailField.css({
				'border-color': 'red'
			}).after("<small class='error'>Email is required</small>");


			formIsCorrect = false;
		} else if (!emailField.is(':valid')) {
			emailField.css({
				'border-color': 'red'
			}).after("<small class='error'>This is not an Email</small>");


			formIsCorrect = false;
		}


		if (password.length == 0) {
			confirmPasswordField.css({
				'border-color': 'red'
			});

			passwordField.css({
				'border-color': 'red'
			}).after("<small class='error'>Password is required</small>");


			formIsCorrect = false;
		} else if (password.length < 6) {
			passwordField.css({
				'border-color': 'red'
			}).after("<small class='error'>Password must be at least 6 characters</small>");


			formIsCorrect = false;
		}


		if (password != confirmPassword) {
			passwordField.css({
				'border-color': 'red'
			});

			confirmPasswordField.css({
				'border-color': 'red'
			}).after("<small class='error'>Passwors don\'t match</small>");


			formIsCorrect = false;
		}


		if (formIsCorrect) {
			$('#sign-up-form').submit();
		}
	});
});