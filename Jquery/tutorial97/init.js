$('#btn').click(function(){

	var value = $("#username").val();

	$.get("server file path", { input: value }, function(data){

		$("#feedback").text(data);

	});

});