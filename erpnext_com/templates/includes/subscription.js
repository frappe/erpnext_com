frappe.ready(function() {
	let $page = $('#page-signup, #page-signup-1');
	$page.find('input[name="email"]').on('change', function() {
		let email = $(this).val();
		if(!valid_email(email)) {
			$(this).closest('.form-group').addClass('invalid');
		} else {
			$(this).closest('.form-group').removeClass('invalid');
		}
	});

	$page.find('.subscribe-button').on('click', () => {
		if(!$page.find('input[name="full_name"]').val()
			|| !$page.find('input[name="email"]').val()
			|| $page.find('input[name="email"]').parent().hasClass('invalid')
			|| $page.find('input[name="passphrase"]').parent().hasClass('invalid')
			|| !$page.find('select[name="industry_type"]').val()
			|| !$page.find('input[name="passphrase"]').val() ) {

			frappe.msgprint("All fields are necessary. Please try again.");
			return false;
		} else {
			show_subscription_form();
		}
	});

	function show_subscription_form() {
		$page.find('.personal-info').addClass('hide');
		$page.find('.subscription').removeClass('hide');

		$page.find('.stage-2').addClass('completed');
		$page.find('.stage-name-subscription').removeClass('text-extra-muted');
	}

	setup_signup($('#page-signup'));

	let plan_name = frappe.utils.get_query_params().plan;

	if(plan_name) {
		frappe.call({
			method: 'erpnext_com.www.pricing.index.get_plan_details',
			args: { plan_name },
			callback: function(r) {
				if (r.exc) return;

				if (r.message) {
					plan = r.message
					window.plan = plan;
					let pricing = plan.pricing;

					$('.plan-name').html('ERPNext ' + plan_name.replace('P-', ''));
					$('.pricing-currency').html(pricing.symbol);

					$('.monthly-pricing, .total-cost').html(pricing.monthly_amount );
				}
			},

		});
	}

	frappe.call({
		method:"erpnext_com.api.load_dropdowns",
		callback: function(r) {
			let $country_select = $("select[name*='country']");
			r.message.countries.forEach(country_name => {
				$country_select.append($("<option />").val(country_name).text(country_name));
			});

			let $language_select = $("select[name*='language']");
			r.message.languages.forEach(language => {
				$language_select.append($("<option />").val(language).text(language));
			});

			let $timezone_select = $("select[name*='timezone']");
			r.message.all_timezones.forEach(timezone => {
				$timezone_select.append($("<option />").val(timezone).text(timezone));
			});

			let $currency_select = $("select[name*='currency']");
			r.message.currencies.forEach(currency => {
				$currency_select.append($("<option />").val(currency).text(currency));
			});

			let country_info = r.message.country_info;

			$country_select.on('change', function() {
				let country = $(this).val();
				$timezone_select.val(country_info[country].timezones[0]);
				$currency_select.val(country_info[country].currency);
			});

			$language_select.val('English');
			if(r.message.default_country) {
				$country_select.val(r.message.default_country);
			} else {
				$country_select.val('India');
			}
			$country_select.trigger('change');
		}
	});

});

setup_signup = function(page) {
	// button for signup event
	if (!page) {
		// fallback
		var page = $('#page-signup,#page-signup-1');
	}

	$('input[name="number_of_users"]').val(1);

	$('input[name="number_of_users"]').on('change', function() {
		let number_of_users = Number($(this).val());

		if(isNaN(number_of_users) || number_of_users <= 0) {
			$(this).closest('.form-group').addClass('invalid');
		} else {
			$(this).closest('.form-group').removeClass('invalid');

			$('.number_of_users').html(number_of_users);
			$('.user-text').html(number_of_users > 1 ? 'users' : 'user');
			$('.total-cost').html((plan.pricing.monthly_amount * number_of_users).toFixed(0));
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
		var args = Array.from(page.find('form input, form select'))
			.reduce(
				(acc, input) => {
					acc[$(input).attr('name')] = $(input).val();
					return acc;
				}, {});
		args.subdomain = args.subdomain.toLowerCase();

		// all mandatory
		if(!(args.full_name && args.email && args.number_of_users && args.subdomain
				&& args.language && args.country && args.timezone && args.currency
				&& args.passphrase && args.industry_type && args.number_of_users)) {
			frappe.msgprint("All fields are necessary. Please try again.");
			return false;
		}

		// validate inputs
		const validations = Array.from(page.find('.form-group.invalid'))
			.map(form_group => $(form_group).find('.validation-message').html());
			if(validations.length > 0) {
			frappe.msgprint(validations.join("<br>"));
			return;
		}

		if($("input[name*='agree-checkbox']").prop("checked") === false) {
			frappe.msgprint("Please agree to the Terms of Use and Privacy Policy.");
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
		var url = window.erpnext_signup.distribution=='schools' ? "/schools/pricing" : '/pricing';
		window.location.href = url + '?' + $.param( query_params )

	} else {
		if (query_params.for_mobile_app) {
			// for mobile app singup, hide header and footer
			$("header,footer").addClass("hidden");
		}

		$('.plan-name').html(query_params.plan);
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

	window.clear_timeout = function() {
		if (window.timout_password_strength) {
			clearTimeout(window.timout_password_strength);
			window.timout_password_strength = null;
		}
	};

	window.strength_indicator = $('.password-strength-indicator');
	window.strength_message = $('.password-strength-message');

	$('#passphrase').on('keyup', function() {
		window.clear_timeout();
		window.timout_password_strength = setTimeout(test_password_strength, 200);
	});

	function test_password_strength(){
		window.timout_password_strength = null;
		return frappe.call({
			type: 'GET',
			method: 'frappe.core.doctype.user.user.test_password_strength',
			args: {
				new_password: $('#passphrase').val()
			},
			callback: function(r) {
				if (r.message) {
					var score = r.message.score,
						feedback = r.message.feedback;

					feedback.crack_time_display = r.message.crack_time_display;
					feedback.score = score;

					if(feedback.password_policy_validation_passed){
						set_strength_indicator('green', feedback);
						$('input[name="passphrase"]').closest('.form-group').removeClass('invalid');
					} else {
						set_strength_indicator('red', feedback);
						$('input[name="passphrase"]').closest('.form-group').addClass('invalid');
					}
				}
			}
		});
	}

	function set_strength_indicator(color, feedback) {
		var message = [];
		feedback.help_msg = "";
		if(!feedback.password_policy_validation_passed){
			feedback.help_msg = "<br>" + "{{ _("Hint: Include symbols, numbers and capital letters in the password") }}";
		}
		if (feedback) {
			if(!feedback.password_policy_validation_passed){
				if (feedback.suggestions && feedback.suggestions.length) {
					message = message.concat(feedback.suggestions);
				} else if (feedback.warning) {
					message.push(feedback.warning);
				}
				message.push(feedback.help_msg);

			} else {
				message.push("{{ _('Success! You are good to go 👍') }}");
			}
		}

		strength_indicator.removeClass().addClass('password-strength-indicator indicator ' + color);
		strength_message.html(message.join(' ') || '').removeClass('hidden');
		// strength_indicator.attr('title', message.join(' ') || '');
	}

};
