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
		if(!(args.full_name && args.company_name && args.email && args.subdomain)) {
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

		args.cmd = "frappe_central.frappe_central.doctype.frappe_account_request.frappe_account_request.sign_up";

		var btn_html = $(".btn-request").html();
		$(".btn-request").prop("disabled", true).html("Sending details...");

        goog_report_conversion()

		// on success, it will show message page!
		$.ajax({
			url: "/",
			data: args,
			type: "POST",
			statusCode: {
				200: function(data, status, xhr) {
					if (status==="success") {
						document.open();
						document.write(data);
						document.close();
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

// var set_distribution = function(toggle) {
// 	if (!window.erpnext_distribution) {
// 		window.erpnext_distribution = get_query_params().distribution || "erpnext";
// 	}
//
// 	if (toggle) {
// 		if (window.erpnext_distribution === "erpnext") {
// 			window.erpnext_distribution = "schools";
// 		} else {
// 			window.erpnext_distribution = "erpnext";
// 		}
// 	}
//
// 	var distribution_title, company_placeholder, company_label;
// 	if (window.erpnext_distribution=='erpnext') {
// 		distribution_title = 'ERPNext';
// 		company_placeholder = 'My Company'
// 		company_label = ''
// 	} else {
// 		distribution_title =
// 		company_placeholder =
// 		company_label =
// 	}
//
// 	$(".erpnext-distribution").html(distribution_title);
//
// 		{
// 		"erpnext": "ERPNext",
// 		"schools": "ERPNext Schools <sup class='text-warning' style='font-weight: 300;'>beta</sup>"
// 	}[window.erpnext_distribution]);
//
// 	company_placeholder = {}
//
// 	$('[data-field-section="company_name"')
// 		.find('.form-control').attr('placeholder', company_placeholder).end()
// 		.find('.help-block').text(company_label)
// }
