$(document).ready(function(){
	jQuery.fn.isChildOf = function(b){ 
    	return (this.parents(b).length > 0); 
	};
	
	$(".gamedetailentry").hide();

	$(".tab").click(function() {
		$(".gamedetailentry").animate({width: 'hide'});
		
		if ($('> #steamtab', this).length && $(this).prev().is(":visible")) {
			$("#steamtab").css('border-left', '2px solid black');
		} else if ($('> #steamtab', this).length) {
			$("#steamtab").css('border-left', '0');
		} else {
			$("#steamtab").css('border-left', '2px solid black'); 
		};
		
		if($(this).prev().is(":visible")) {
			$(this).prev().animate({width: 'hide'});
			return false;
		};
		
		$(this).prev().animate({width: 'show'});
		
	});

});
