$(':button').click(function(){
	$(':button').attr("value","Hello");
});

$(':submit').click(function(){
	$(this).attr("value","I am clicked");
});