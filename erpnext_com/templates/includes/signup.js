setup_signup = function(page) {
	// button for signup event
	if (!page) {
		// fallback
		var page = $('#page-signup,#page-signup-1');
	}

	page.find('.btn-request').off('click').on('click', function() {
		var args = {};
		$.each(page.find("form input"), function(i, input) {
			args[$(input).attr("name")] = $(input).val();
		});


		// all mandatory
		if(!(args.full_name && args.email && args.subdomain)) {
			frappe.msgprint("All fields are necessary. Please try again.");
			return false;
		}

		// email is valid
		if(!valid_email(args.email)) {
			frappe.msgprint('Please enter a valid Email Address.');
			return false;
		}

		// subdomain in one word
		if(args.subdomain.search(/^[a-z0-9][-a-z0-9]*[a-z0-9]$/)===-1) {
			frappe.msgprint("Sub-domain can only contain letters, numbers and hyphens. Please try again.");
			return false;
		}

		var MAX_LENGTH = 20;
		if(args.subdomain.length > MAX_LENGTH) {
			frappe.msgprint("Sub-domain can not have more than " + MAX_LENGTH + " characters.");
			return false;
		}

		// add plan to args
		var plan = get_url_arg('plan');
		if(plan) args.plan = plan;

		args.distribution = window.erpnext_signup.distribution;

		args.cmd = "erpnext_com.api.signup";

		var btn_html = $(".btn-request").html();
		$(".btn-request").prop("disabled", true).html("Sending details...");

        goog_report_conversion()

		// on success, it will show message page!
		$.ajax({
			url: "/",
			data: args,
			type: "POST",
			statusCode: {
				200: function(data, success, xhr) {
					if (data.message && data.message.location) {
						window.location.href = data.message.location;
					}
				}
			}
		}).fail(function(xhr) {
			var data = JSON.parse(xhr.responseText);
			if(data.message) {
				frappe.msgprint(data.message);
			} else {
				var message = data._server_messages ? JSON.parse(data._server_messages).join("\n")
					: "Some error occured. Please try again.";
				frappe.msgprint(message);
			}

			if(data.exc) {
				console.error(JSON.parse(data.exc).join("\n"));
			}

		}).always(function() {
			console.log('always', arguments);
			$(".btn-request").prop("disabled", false).html(btn_html);
		});

		return false;
	});


	// change help description based on subdomain change
	$('[name="subdomain"]').on("keyup", function() {
		$('.subdomain-help').text($(this).val() || window.erpnext_signup.subdomain_placeholder);
	});

	// distribution
	// $('.erpnext-distribution').on("click", function() {
	// 	set_distribution(true);
	// });
	//
	// set_distribution();

	var query_params = get_query_params();
	if (!query_params.plan) {
		// redirect to pricing page
		window.location.href = window.erpnext_signup.distribution=='schools' ? "/schools/pricing" : '/pricing';
	} else if (query_params.for_mobile_app) {
		// for mobile app singup, hide header and footer
		$("header,footer").addClass("hidden");
	}

	if (["Free", "Free-Solo"].indexOf(query_params.plan)!==-1) {
		page.find(".plan-message").text("Free for 1 User");
	} else {
		page.find(".plan-message").text("Free 30-day Trial");
	}

	$('.domain-missing-msg').addClass("hidden");
	if (query_params.domain) {
		var subdomain = query_params.domain;
		if (subdomain.indexOf(".{{ frappe.local.conf.domain }}")) {
			subdomain = subdomain.replace(".{{ frappe.local.conf.domain }}", "");
		}
		$('[name="subdomain"]').val(subdomain);

		$('.missing-domain').html(query_params.domain);
		$('.missing-domain-msg').removeClass("hidden");
	}

};
