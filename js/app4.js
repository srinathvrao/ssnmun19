validAppDel = angular.module('validAppDel', []);
validAppDel.controller('DelController', function($scope) {
	
	$scope.submitForm = function(isValid) {

		function showThanks() {
			$("#reg-del").modal('hide');
			$('#post-sub').modal('show');
		}

		function postToGoogle() {

			var appl = $('#nameDel').val();
			var college = $('#collegeDel').val();
			var phone = $('#phone-noDel').val();
			var email = $('#emailDel').val();
			var fb = $('#fb-idDel').val();
			var no_del = $('#no-delDel').val();
			var exp = $('#expDel').val();
			var comPref1 = $('#comPref1').val();
			var countryPref1 = $('#countryPref1').val();
			var comPref2 = $('#comPref2').val();
			var countryPref2 = $('#countryPref2').val();
			var comPref3 = $('#comPref3').val();
			var countryPref3 = $('#countryPref3').val();
			var shirt = $('#shirtDel:checked').val();
			var size = $('#sizeDel').val();
			
			if(shirt != 'on') {
				shirt = "NO";
				size = "---";
			}
			else
				shirt = "YES";

			$.ajax({
				url: "https://docs.google.com/forms/d/1eys-zH9lGEzMY6ORjka7fVdBLoETTUCt-i7aEH_WGdg/formResponse",
				data: {
					"entry.1786824178": appl,
					"entry.1940540313": college,
					"entry.2010857297": phone,
					"entry.1281746893": email,
					"entry.769454632": fb,
					"entry.273268553": no_del,
					"entry.339412521": exp,
					"entry.215829800": comPref1,
					"entry.753046658": countryPref1,
					"entry.2092424956": comPref2,
					"entry.1208838674": countryPref2,
					"entry.2006279503": comPref3,
					"entry.116579876": countryPref3,
					"entry.56274900": shirt,
					"entry.1442238991": size,
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
						alert("Error 404: Google Sheet Entry Failed\nPlease Confirm Submission");
					}
				}
			});
		}

		function backupMail() {
			$.ajax({
				type: "POST",
				url: "mail-del.php",
				data: $('form.formDel').serialize(),
				success: function() {
					;
				},
				error: function(){
					;
				}
			});
		}

		function validCountries() {
			var com1 = document.getElementById("country-matrix-"+$('#comPref1').val()).options;
			var country1 = $('#countryPref1').val();
			for(var i=0;i<com1.length;++i)
				if(com1[i].value == country1)
					break;
			if(i == com1.length) {
				alert("Country Preference 1 is not in corresponding list.\nPlease enter a valid country");
				return false;
			}
			
			var com2 = document.getElementById("country-matrix-"+$('#comPref2').val()).options;
			var country2 = $('#countryPref2').val();
			for(i=0;i<com2.length;++i)
				if(com2[i].value == country2)
					break;
			if(i == com2.length) {
				alert("Country Preference 2 is not in corresponding list.\nPlease enter a valid country");
				return false;
			}

			var com3 = document.getElementById("country-matrix-"+$('#comPref3').val()).options;
			var country3 = $('#countryPref3').val();
			for(i=0;i<com3.length;++i)
				if(com3[i].value == country3)
					break;
			if(i == com1.length) {
				alert("Country Preference 3 is not in corresponding list.\nPlease enter a valid country");
				return false;
			}

			return true;

		}

		if(isValid && validCountries()==true) {
			postToGoogle();
			backupMail();
		}
	};
});

validAppIP = angular.module('validAppIP', []);
validAppIP.controller('IPController', function($scope) {

	$scope.submitForm = function(isValid) {

		function showThanks() {
			$("#IP-reg").modal('hide');
			$('#post-sub').modal('show');
		}

		function postToGoogle() {

			var appl = $('#nameIP').val();
			var college = $('#collegeIP').val();
			var phone = $('#phone-noIP').val();
			var email = $('#emailIP').val();
			var fb = $('#fb-idIP').val();
			var no_ip = $('#no-ipIP').val();
			var exp = $('#expIP').val();
			var comPref1 = $('#comPref1IP').val();
			var comPref2 = $('#comPref2IP').val();
			var comPref3 = $('#comPref3IP').val();
			var shirt = $('#shirtIP:checked').val();
			var size = $('#sizeIP').val();
			
			if(shirt != 'on') {
				shirt = "NO";
				size = "---";
			}
			else
				shirt = "YES";

			$.ajax({
				url: "https://docs.google.com/forms/d/1DnFreltqQIIiXFJQc_hRuuD299SFqRPx5g2Sv-MgbsY/formResponse",
				data: {
					"entry.2006319896": appl,
					"entry.1956858739": college,
					"entry.1130045011": phone,
					"entry.1874693604": email,
					"entry.251252728": fb,
					"entry.803391573": no_ip,
					"entry.1033512323": exp,
					"entry.1862407481": comPref1,
					"entry.2025821485": comPref2,
					"entry.1823730254": comPref3,
					"entry.1726842162": shirt,
					"entry.262718237": size,
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
				url: "mail-ip.php",
				data: $('form.formIP').serialize(),
				success: function() {
					;
				},
				error: function(){
					;
				}
			});
		}

		if(isValid) {
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
	var dvDel = document.getElementById('regDel');
	angular.bootstrap(dvDel, ['validAppDel']);
	var dvIP = document.getElementById('regIP');
	angular.bootstrap(dvIP, ['validAppIP']);
	var dvMsg = document.getElementById('dvMsg');
	angular.bootstrap(dvMsg, ['messageApp']);
});