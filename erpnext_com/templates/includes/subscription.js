setup_signup = function(page) {
	// button for signup event
	if (!page) {
		// fallback
		var page = $('#page-signup,#page-signup-1');
	}

	let domain_input_flag = 0;

	$('input[name="number_of_users"]').on('change', function() {
		let number_of_users = Number($(this).val());

		if(isNaN(number_of_users) || number_of_users <= 0) {
			$(this).closest('.form-group').addClass('invalid');
		} else {
			$(this).closest('.form-group').removeClass('invalid');

			$('.subscription-price').html((19.99 * number_of_users).toFixed(2));
		}
	});

	page.find('input[name="subdomain"]').on('input', function() {
		domain_input_flag = 1;
		var $this = $(this);
		clearTimeout($this.data('timeout'));
		$this.data('timeout', setTimeout(function() {
			let subdomain = $this.val();
			set_availability_status('empty');
			if(subdomain.length === 0) {
				return;
			}

			page.find('.availability-status').addClass('hidden');
			var [is_valid, validation_msg] = is_a_valid_subdomain(subdomain);
			if(is_valid) {
				// show spinner
				page.find('.availability-spinner').removeClass('hidden');
				check_if_available(subdomain, function(status) {
					set_availability_status(status, subdomain);
					// hide spinner
					page.find('.availability-spinner').addClass('hidden');
				});
			} else {
				set_availability_status('invalid', subdomain, validation_msg);
			}
		}, 500));
	});

	function set_availability_status(is_available, subdomain, validation_msg) {
		// reset
		page.find('.availability-status').addClass('hidden');
		page.find('.signup-subdomain').removeClass('invalid');

		if(typeof is_available === 'string') {
			if(is_available === 'empty') {
				// blank state
			} else if(is_available === 'invalid') {
				// custom validation message
				const form_control = page.find('.signup-subdomain').addClass('invalid');
				form_control.find('.validation-message').html(validation_msg || '');
			}
			return;
		}

		page.find('.availability-status').removeClass('hidden');
		if(is_available) {
			// available state
			page.find('.availability-status i').removeClass('octicon-x text-danger');
			page.find('.availability-status i').addClass('octicon-check text-success');

			page.find('.availability-status').removeClass('text-danger');
			page.find('.availability-status').addClass('text-success');
			page.find('.availability-status span').html(`${subdomain}.erpnext.com is available!`);
		} else {
			// not available state
			page.find('.availability-status i').removeClass('octicon-check text-success');
			page.find('.availability-status i').addClass('octicon-x text-danger');

			page.find('.availability-status').removeClass('text-success');
			page.find('.availability-status').addClass('text-danger');
			page.find('.availability-status span').html(`${subdomain}.erpnext.com is already taken.`);
		}
	}

	page.find('.btn-request').off('click').on('click', function() {
		var args = Array.from(page.find('form input'))
			.reduce(
				(acc, input) => {
					acc[$(input).attr('name')] = $(input).val();
					return acc;
				}, {});
		args.subdomain = args.subdomain.toLowerCase();

		// all mandatory
		if(!(args.full_name && args.email && args.company_name && args.subdomain)) {
			frappe.msgprint("All fields are necessary. Please try again.");
			return false;
		}

		// validate inputs
		const validations = Array.from(page.find('.form-group.invalid'))
			.map(form_group => $(form_group).find('.validation-message').html());
		// console.log(validations)
		if(validations.length > 0) {
			frappe.msgprint(validations.join("<br>"));
			return;
		}

		// add plan to args
		var plan = frappe.utils.get_url_arg('plan');
		if(plan) args.plan = plan;

		var res = frappe.utils.get_url_arg('res');
		if(res) args.res = res;

		args.distribution = window.erpnext_signup.distribution;

		var $btn = $('.btn-request');

		var btn_html = $btn.html();
		$btn.prop("disabled", true).html("Sending details...");

		goog_report_conversion(); // eslint-disable-line


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

	function is_a_valid_subdomain(subdomain) {
		var MIN_LENGTH = 4;
		var MAX_LENGTH = 20;
		if(subdomain.length < MIN_LENGTH) {
			return [0, `Sub-domain cannot have less than ${MIN_LENGTH} characters`];
		}
		if(subdomain.length > MAX_LENGTH) {
			return [0, `Sub-domain cannot have more than ${MAX_LENGTH} characters`];
		}
		if(subdomain.search(/^[A-Za-z0-9][-A-Z-a-z0-9]*[A-Za-z0-9]$/)===-1) {
			return [0, 'Sub-domain can only contain letters and numbers'];
		}
		return [1, ''];
	}

	function check_if_available(subdomain, callback) {
		setTimeout(function() {
			frappe.call({
				method: 'erpnext_com.api.check_subdomain_availability',
				args: { subdomain: subdomain },
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

	var query_params = frappe.utils.get_query_params();
	if (!query_params.plan) {
		// redirect to pricing page
		// var url = window.erpnext_signup.distribution=='schools' ? "/schools/pricing" : '/pricing';
		// window.location.href = url + '?' + $.param( query_params )

	} else if (query_params.for_mobile_app) {
		// for mobile app singup, hide header and footer
		$("header,footer").addClass("hidden");
	}

	page.find(".plan-message").text("Free 30-day Trial");

	// if (['Free', 'Free-Solo'].indexOf(query_params.plan)!==-1) {
// 		// keeping Free-Solo for backward compatibility
// 		page.find(".plan-message").text("Free for 1 User");
// 	}

	$('.domain-missing-msg').addClass("hidden");
	if (query_params.domain) {
		var subdomain = query_params.domain;
		if (subdomain.indexOf(".{{ signup_domain }}")) {
			subdomain = subdomain.replace(".{{ signup_domain }}", "");
		}
		$('[name="subdomain"]').val(subdomain);

		$('.missing-domain').html(query_params.domain);
		$('.missing-domain-msg').removeClass("hidden");
	}

};
