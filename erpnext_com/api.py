from __future__ import unicode_literals
import frappe
from frappe import _
import requests

@frappe.whitelist(allow_guest=True)
def signup(full_name, email, subdomain, plan="Free-Solo", distribution="erpnext"):
	central_url = frappe.local.conf.central_url or 'https://central.erpnext.com'

	# send request to central
	r = requests.post(central_url.rstrip('/ ') + '/api/method/central.signup.signup', data={
		'full_name': full_name,
		'email': email,
		'subdomain': subdomain,
		'plan': plan,
		'distribution': distribution
	})

	context = {
		'pathname': 'schools/signup' if distribution=='schools' else 'signup'
	}

	if r.status_code == 200:
		location = frappe.redirect_to_message(_('Thank you for signing up'),
			"""<div><p>You will receive an email at {},
			asking you to verify this account request.<br>
			If you are unable to find the email in your inbox, please check your SPAM folder.
			It may take a few minutes before you receive this email.</p>
			<p>Once you click on the verification link, your account will be ready in a few minutes.</p>
			</div>""".format(email), context=context)

	else:
		# something went wrong
		location = frappe.redirect_to_message(_('Something went wrong'),
			'Please try again or drop an email to support@erpnext.com',
			context=context, http_status_code=500)

	print location
	return {
		'location': location
	}

