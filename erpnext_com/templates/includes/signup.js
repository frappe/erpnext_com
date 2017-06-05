setup_signup = function(page) {
	// button for signup event
	if (!page) {
		// fallback
		var page = $('#page-signup,#page-signup-1');
	}

	const email_domains = {
		"gmail": "https://mail.google.com/",
		"yahoo": "https://mail.yahoo.com/"
	}

	let domain_input_flag = 0;

	// page.find('.signup-state-details input').on('input change blur', function() {
	// 	$btn = page.find('.btn-request');
	// 	if(page.find('.invalid').length) {
	// 		$btn.addClass('inactive');
	// 		return;
	// 	}
	// 	page.find('.signup-state-details input').each(function(item) {
	// 		if($(this).val().length === 0) {
	// 			$btn.addClass('inactive');
	// 		} else {
	// 			$btn.removeClass('inactive');
	// 		}
	// 	});
	// });

	page.find('input[name="email"]').on('change', function() {
		let email = $(this).val();
		if(!valid_email(email)) {
			$(this).closest('.form-group').addClass('invalid');
		} else {
			$(this).closest('.form-group').removeClass('invalid');
		}
	})

	page.find('input[name="company_name"]').on('input', function() {
		var $this = $(this);
		clearTimeout($this.data('timeout'));
		$this.data('timeout', setTimeout(function() {
			// remove only problematic chars
			let subdomain = $this.val().toLowerCase().replace(/[^a-z]/g, '');
			if(subdomain.length === 0) return;

			// Set only if not previously set by the user or domain empty
			if(is_a_valid_subdomain(subdomain)[0] &&
				(page.find('input[name="subdomain"]').val().length === 0 ||
					domain_input_flag === 0)) {

				check_if_available(subdomain, function(status) {
					if(status) {
						page.find('.signup-subdomain').removeClass('invalid');
						page.find('input[name="subdomain"]').val(subdomain).trigger('change');
						domain_input_flag = 0;

						page.find('.availability-status i').addClass('octicon-check text-success');
						page.find('.availability-status i').removeClass('octicon-x text-danger');
						page.find('.availability-status').removeClass('hidden');
					}
				});
			}
		}, 500));
	})

	page.find('input[name="subdomain"]').on('input', function() {
		domain_input_flag = 1;
		var $this = $(this);
		clearTimeout($this.data('timeout'));
		$this.data('timeout', setTimeout(function() {
			let subdomain = $this.val();
			if(subdomain.length === 0) return;
			// $this.closest('.form-group').removeClass('invalid');

			page.find('.availability-status').addClass('hidden');
			var is_valid = is_a_valid_subdomain(subdomain);
			if(is_valid[0]) {
				$this.closest('.form-group').removeClass('invalid');
				page.find('.availability-spinner').removeClass('hidden');
				check_if_available(subdomain, function(status) {
					if(status) {
						page.find('.availability-status i').removeClass('octicon-x text-danger');
						page.find('.availability-status i').addClass('octicon-check text-success');

						page.find('.availability-status').removeClass('text-danger');
						page.find('.availability-status').addClass('text-success');
						page.find('.availability-status span').html(`${subdomain}.erpnext.com is available!`);
					} else {
						page.find('.availability-status i').removeClass('octicon-check text-success');
						page.find('.availability-status i').addClass('octicon-x text-danger');

						page.find('.availability-status').removeClass('text-success');
						page.find('.availability-status').addClass('text-danger');
						page.find('.availability-status span').html(`${subdomain}.erpnext.com is already taken.`);
					}
					page.find('.availability-spinner').addClass('hidden');
					page.find('.availability-status').removeClass('hidden');
				});
			} else {
				$this.parent().siblings('.validation-message').html(is_valid[1]);
				$this.closest('.form-group').addClass('invalid');
			}
		}, 500));
	})

	page.find('.btn-request').off('click').on('click', function() {
		var args = {};
		$.each(page.find("form input"), function(i, input) {
			args[$(input).attr("name")] = $(input).val();
		});
		args["subdomain"] = args.subdomain.toLowerCase();

		//
		// // all mandatory
		// if(!(args.full_name && args.email && args.company && args.subdomain)) {
		// 	frappe.msgprint("All fields are necessary. Please try again.");
		// 	return false;
		// }

		// // email is valid
		// if(!valid_email(args.email)) {
		// 	frappe.msgprint('Please enter a valid Email Address.');
		// 	return false;
		// }

		// subdomain in one word
		// if(args.subdomain.search(/^[a-z0-9][-a-z0-9]*[a-z0-9]$/)===-1) {
		// 	frappe.msgprint("Sub-domain can only contain letters, numbers and hyphens. Please try again.");
		// 	return false;
		// }

		// var MAX_LENGTH = 20;
		// if(args.subdomain.length > MAX_LENGTH) {
		// 	frappe.msgprint("Sub-domain can not have more than " + MAX_LENGTH + " characters.");
		// 	return false;
		// }

		// add plan to args
		var plan = get_url_arg('plan');
		if(plan) args.plan = plan;

		var res = get_url_arg('res');
		if(res) args.res = res;

		args.distribution = window.erpnext_signup.distribution;

		var $btn = $('.btn-request');

		var btn_html = $btn.html();
		$btn.prop("disabled", true).html("Sending details...");

        goog_report_conversion();

		console.log("BEFORE SENDING");

		// on success, it will show message page!
		frappe.call({
			method: 'erpnext_com.api.signup',
			args: args,
			type: 'POST',
			btn: $btn,
			callback: function(r) {
				if (r.exc) return;

				if (r.message.location) {
					window.location.href = r.message.location;
				}
			},

		}).always(function() {
			$btn.prop("disabled", false).html(btn_html);
		})

		// Do directly on verification message page, not here

		// var verification_msg = `We've sent an email to ${args.email}. Please `;
		// Object.keys(email_domains).map(function(domain) {
		// 	if(args.email.includes(domain)) {
		// 		verification_msg += `login to <a href="${email_domains[domain]}">${domain}</a> and `;
		// 	}
		// });

		// verification_msg += `follow the link to verify your account request.`;

		// page.find('.signup-process-message').html(verification_msg);

		// page.find('.signup-state-details').addClass("hidden");
		// page.find('.signup-state-verification').removeClass("hidden");

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

	function is_a_valid_subdomain(subdomain) {
		var MIN_LENGTH = 4;
		var MAX_LENGTH = 20;
		if(subdomain.length < MIN_LENGTH) {
			return [0, `Sub-domain cannot have less than ${MIN_LENGTH} characters`];
		}
		if(subdomain.length > MAX_LENGTH) {
			return [0, `Sub-domain cannot have more than ${MAX_LENGTH} characters`];
		}
		if(subdomain.search(/^[a-z0-9][-a-z0-9]*[a-z0-9]$/)===-1) {
			return [0, 'Sub-domain can only contain letters, numbers and hyphens'];
		}
		return [1, ''];
	}

	function check_if_available(subdomain, callback) {
		setTimeout(function() {
			frappe.call({
				method: 'erpnext_com.api.check_subdomain_availability',
				args: {subdomain: subdomain},
				type: 'POST',
				callback: function(r) {
					if(!r.message) {
						callback(1);
					} else {
						callback(0);
					}
				},
			});
		}, 2000);
	}

	var query_params = get_query_params();
	if (!query_params.plan) {
		// redirect to pricing page
		var url = window.erpnext_signup.distribution=='schools' ? "/schools/pricing" : '/pricing';
		window.location.href = url + '?' + $.param( query_params )

	} else if (query_params.for_mobile_app) {
		// for mobile app singup, hide header and footer
		$("header,footer").addClass("hidden");
	}

	if (['Free', 'Free-Solo'].indexOf(query_params.plan)!==-1) {
		// keeping Free-Solo for backward compatibility
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
