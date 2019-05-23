var validAppEB = angular.module('validAppEB', []);
validAppEB.controller('EBController', function($scope) {
	// function to submit the form after all validation has occurred			
	$scope.submitForm = function(isValid) {
		// check to make sure the form is completely valid

		if (isValid) {
			$.ajax({
				type: "POST",
				url: "reg-eb.php",
				data: $('form.formEB').serialize(),
				success: function() {
					$("#EB-reg").modal('hide');
					$('#post-sub').modal('show');
				},
				error: function(){
					alert("failure");
				}
			});
		}
	};
});

var validAppPH = angular.module('validAppPH', []);
validAppPH.controller('PHController', function($scope) {

	// function to submit the form after all validation has occurred			
	$scope.submitForm = function(isValid) {
		// check to make sure the form is completely valid
		if (isValid) {
			$.ajax({
				type: "POST",
				url: "reg-ip-head.php",
				data: $('form.formPH').serialize(),
				success: function() {
					$("#IP-head-reg").modal('hide');
					$('#post-sub').modal('show');
				},
				error: function(){
					alert("failure");
				}
			});
		}
	};
});

var messageApp = angular.module('messageApp', []);
messageApp.controller('mgController', function($scope) {

	// function to submit the form after all validation has occurred			
	$scope.submitForm = function(isValid) {
		// check to make sure the form is completely valid
		if (isValid) {
			$.ajax({
				type: "POST",
				url: "mail.php",
				data: $('form.formMsg').serialize(),
				success: function() {
					$('.formMsg input').attr('value','');
					alert("Message Sent!");
				},
				error: function(){
					alert("failure");
				}
			});
		}
	};
});

angular.element(document).ready(function() {
	var dvEB = document.getElementById('regEB');
	angular.bootstrap(dvEB, ['validAppEB']);
	var dvIPH = document.getElementById('regIPH');
	angular.bootstrap(dvIPH, ['validAppPH']);
	var dvMsg = document.getElementById('dvMsg');
	angular.bootstrap(dvMsg, ['messageApp']);
});