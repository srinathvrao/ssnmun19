validAppEB = angular.module('validAppEB', []);
validAppEB.controller('EBController', function($scope) {
	$scope.submitForm = function(isValid) {

		function showThanks() {
			$("#EB-reg").modal('hide');
			$('#post-sub').modal('show');
		}

		function postToGoogle() {

			var appl = $('#nameEB').val();
			var college = $('#collegeEB').val();
			var phone = $('#phone-noEB').val();
			var email = $('#emailEB').val();
			var fb = $('#fb-idEB').val();
			
			var no_del = $('#no-delEB').val();
			var exp_del = $('#exp-delEB').val();
			var no_eb = $('#no-ebEB').val();
			var exp_eb = $('#exp-ebEB').val();
			var exp_oc = $('#exp-ocEB').val();
			var exp_other = $('#exp-otherEB').val();
			
			var com_pref_1 = $('#1-pref-comEB').val();
			var pos_pref_1 = $('#1-pref-posEB').val();
			var com_pref_2 = $('#2-pref-comEB').val();
			var pos_pref_2 = $('#2-pref-posEB').val();
			var pref_rsn = $('#pref-rsnEB').val();

			$.ajax({
				url: "https://docs.google.com/forms/d/1y06EnI1F3OvnUpI6dIM7XMbzKH40a9eeqaPJY7PbLUg/formResponse",
				data: { "entry.1197343369": appl,
					"entry.1791725144": college,
					"entry.1511185417": phone,
					"entry.1918495440": email,
					"entry.1225606841": fb,
					"entry.891713831": no_del,
					"entry.1173340922": exp_del,
					"entry.2037602734": no_eb,
					"entry.504281787": exp_eb,
					"entry.393346440": exp_oc,
					"entry.1286179937": exp_other,
					"entry.1242750387": com_pref_1,
					"entry.69310692": pos_pref_1,
					"entry.561725342": com_pref_2,
					"entry.1671190613": pos_pref_2,
					"entry.434375508": pref_rsn,
				},
				type: "POST",
				dataType: "xml",
				statusCode: {
					0: function() {
						showThanks();
					},
					200: function() {
						showThanks();
					},
					404: function() {
						alert("404 Error: Google Sheet Entry Failed\nPlease Confirm Submission");
					}
				}
			});
		}

		function backupMail() {
			$.ajax({
				type: "POST",
				url: "reg-eb.php",
				data: $('form.formEB').serialize(),
				success: function() {
					;
				},
				error: function(){
					alert("Backup Mail Failed");
				}
			});
		}

		if(isValid) {
			postToGoogle();
			backupMail();
		}
	};
});

var validAppPH = angular.module('validAppPH', []);
validAppPH.controller('PHController', function($scope) {

	// function to submit the form after all validation has occurred			
	$scope.submitForm = function(isValid) {
		// check to make sure the form is completely valid

		function showThanks() {
			$("#IP-head-reg").modal('hide');
			$('#post-sub').modal('show');
		}

		function postToGoogle() {

			var appl = $('#nameIPH').val();
			var college = $('#collegeIPH').val();
			var phone = $('#phone-noIPH').val();
			var email = $('#emailIPH').val();
			var fb = $('#fb-idIPH').val();
			
			var no_press = $('#no-pressIPH').val();
			var exp_press = $('#exp-pressIPH').val();
			var no_del = $('#no-delIPH').val();
			var exp_del = $('#exp-delIPH').val();
			var exp_oc = $('#exp-ocIPH').val();
			var exp_jour = $('#exp-jourIPH').val();
			
			var why_me = $('#why-meIPH').val();

			$.ajax({
				url: "https://docs.google.com/forms/d/1PQuf3kTAofTHNd7QVlRg--eU6Cex5m9Xe6wAz1-GaP4/formResponse",
				data: { "entry.902291778": appl,
					"entry.1894599041": college,
					"entry.2072818225": phone,
					"entry.568648210": email,
					"entry.176493194": fb,
					"entry.1428392169": no_press,
					"entry.1601198766": exp_press,
					"entry.866982343": no_del,
					"entry.1206815777": exp_del,
					"entry.2126820737": exp_oc,
					"entry.164667743": exp_jour,
					"entry.1141542482": why_me
				},
				type: "POST",
				dataType: "xml",
				statusCode: {
					0: function() {
						showThanks();
					},
					200: function() {
						showThanks();
					},
					404: function() {
						alert("404 Error: Google Sheet Entry Failed\nPlease Confirm Submission");
					}
				}
			});
		}

		function backupMail() {
			$.ajax({
				type: "POST",
				url: "reg-ip-head.php",
				data: $('form.formPH').serialize(),
				success: function() {
					;
				},
				error: function(){
					alert("Backup Mail Failed");
				}
			});
		}

		if (isValid) {
			postToGoogle();
			backupMail();
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