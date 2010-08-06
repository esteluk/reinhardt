$(document).ready(function(){
	$(".gamedetailentry").hide();

	$(".tab").click(function() {
		var self = this;
		if ($('> #steamtab', this).length && $(this).prev().is(":visible")) {
			$("#steamtab").css('border-left', '2px solid black');
		} else if ($('> #steamtab', this).length) {
			$("#steamtab").css('border-left', '0');
		} else {
			$("#steamtab").css('border-left', '2px solid black'); 
		};
		
		if($(this).prev().is(":visible")) {
			$(this).prev().animate({width: 'hide'}, function() {
				$(this).prevAll(".tab").eq(0).css("background-image", "url('/static/img/vertborderlight.png')");
			});
			return false;
		} else {
			$(".gamedetailentry").animate({width: 'hide'}, function() { 
				$(".tab:last").prevAll(".tab").not($(self).prevAll(".tab").eq(0)).css("background-image", "url('/static/img/vertborderlight.png')");
			});
		};
		
		$(this).prevAll(".tab").eq(0).css("background-image", "url('/static/img/vertborder.png')");
		$(this).prev().animate({width: 'show'});
	});
});
