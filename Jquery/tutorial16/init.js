$(":text").focusin(function(){
	$(this).css("background-color","yellow");
});

$(":text").focusout(function(){
	$(this).css("background-color","#fff");
	$('#para').css("background-color","red").css("color","#fff");
});