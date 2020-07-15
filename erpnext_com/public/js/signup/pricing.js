frappe.ready(function () {
	function set_expiry(key, value, period) {
		// convert days to milliseconds, faster than importing external library
		period = period * 86400000;
		const now = new Date();

		const value_obj = {
			value: value,
			expiry: now.getTime() + period,
		};
		localStorage.setItem(key, JSON.stringify(value_obj));
	}

	var referral_id = frappe.utils.get_url_arg('referral-id');
	if (referral_id) {
		set_expiry('referral_id', referral_id, 30);
	}
});
