$(document).on("page-change", function(){
	var d = new Date();
	var currentYear = d.getFullYear();
	$("#year").text(currentYear);

	$("#design-slide").addClass("active").css("display","block");

	// footer-link
	$(".footer-link.active").removeClass("active");
	$(".footer-link[href='"+ location.pathname+"']").addClass("active");

	$(".tabs input").click(function(){
	var currentTab = $(".tabs .active");
	var currentFeature = $(".feature.active");
	var newTab = $(this);
	var newFeature = $(".feature#"+this.id+"-slide");

	currentTab.removeClass("active");
	newTab.addClass("active");
	$(".tabs input").attr("disabled","disabled");

	var fadeTime = 250;
	currentFeature.removeClass("active").fadeOut(fadeTime, function(){
		newFeature.addClass("active").fadeIn(fadeTime, function(){
			$(".tabs input").removeAttr("disabled");
			newTab.attr("disabled","disabled");
			});
		});
	});
});

