$(document).ready(function() {
	function workWithFaEye() {
		$('.fa-eye-slash, .fa-eye').off();


		$('.fa-eye-slash').click(function() {
			$('.fa-eye-slash').addClass('fa-eye');
			$('.fa-eye-slash').removeClass('fa-eye-slash');

			$('.fa-eye').css({
				'transform': 'translate(236px, -54px)'
			});

			$('.password-field').attr('type', 'text');

			workWithFaEye();
		});


		$('.fa-eye').click(function() {
			$('.fa-eye').addClass('fa-eye-slash');
			$('.fa-eye').removeClass('fa-eye');

			$('.fa-eye-slash').css({
				'transform': 'translate(235px, -54px)'
			});

			$('.password-field').attr('type', 'password');

			workWithFaEye();
		});
	}

	workWithFaEye();
});