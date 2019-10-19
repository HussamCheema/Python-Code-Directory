$("#button").click(function(){

	var username = $("#username").val();

	$.ajax({

		type: "POST",

		url: 'page.html',

		data: "name="+username,

		dataType:  'json',

		success: function(data){

			$('#content').html(data);

		},
		error: function(x){
			alert("error1");
		}

	});

});