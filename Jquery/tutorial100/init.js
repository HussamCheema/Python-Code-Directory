$('#btn').click(function(){

	var value1 = $("#username").val();
	var value2 = $("#textArea").val();

	$.post("server file path", { input1: value1, input2: value2 }, function(data){

		$("#feedback").html(data);

	}).error(function(){
		alert("Error");
	}).complete(function(){
		alert("Complete");
	}).success(function(){
		alert("Success");
	});

});