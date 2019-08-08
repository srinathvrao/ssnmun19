$.ajax({
	type: "POST",
	url: "api_countries",
	dataType: 'JSON',
	data: s,

	success: function (obj, textstatus) {
		if( !('error' in obj) ) {
			t = obj.text;
		}
		else {
			alert("ERROR!! Please try again later.");
		}
	},
	error: function(XMLHttpRequest, textStatus, errorThrown) {
		alert("An error occurred. Please try again later.");
	}
});