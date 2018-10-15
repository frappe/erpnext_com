from __future__ import unicode_literals
import frappe
from frappe import _
from central.signup import signup as _signup, validate_subdomain
from frappe.integrations.utils import get_checkout_url

# TODO:
# 1. send email to particpant and us
# 2. who is coming page
# 3. final design

@frappe.whitelist(allow_guest=True)
def make_payment(full_name, email, company, workshop=0, conf=0, currency='inr'):
	if currency=='inr':
		conf_rate = 600
		workshop_rate = 2000
	else:
		conf_rate = 10
		workshop_rate = 50

	amount = int(workshop or 0) * workshop_rate + int(conf or 0) * conf_rate

	if not amount:
		frappe.msgprint('Please set no of tickets')
		return

	participant = frappe.get_doc({
		'doctype': 'Conference Participant',
		'full_name': full_name,
		'email_id': email,
		'company_name': company,
		'workshop': workshop,
		'conference': conf,
		'amount': amount
	}).insert(ignore_permissions=True)

	#get controller for respecctive payment gateway
	if currency == "inr":
		payment_gateway = "Razorpay"
	else:
		payment_gateway = "PayPal"

	return get_checkout_url(**{
		"amount": amount,
		"title": 'ERPNext Conference Tickets',
		"description": '{0} passes for conference, {1} passes for workshop'.format(int(conf or 0), int(workshop or 0)),
		"reference_doctype":  participant.doctype,
		"reference_docname": participant.name,
		"payer_email": email,
		"payer_name": full_name,
		"order_id": participant.name,
		"currency": currency,
		"payment_gateway": payment_gateway
	})

@frappe.whitelist(allow_guest=True)
def signup(full_name, email, subdomain, plan=None, distribution="erpnext", res=None, number_of_users=1):
	resp = _signup(full_name, email, subdomain, plan=plan,
		distribution=distribution, reseller=res, users=number_of_users)

	if resp.get("redirect_to"):

		return {
			"location": resp['redirect_to']
		}

	elif resp['status'] == 'success':
		location = frappe.redirect_to_message(_('Verify your Email'),
			"""<div><p>You will receive an email at <strong>{}</strong>,
			asking you to verify this account request.<p><br>
			<p>It may take a few minutes before you receive this email.
			If you don't find it, please check your SPAM folder.</p>
			</div>""".format(email), indicator_color='blue')

	elif resp['status']=='retry':
		return {}

	else:
		# something went wrong
		location = frappe.redirect_to_message(_('Something went wrong'),
			'Please try again or drop an email to support@erpnext.com',
			indicator_color='red')

	return {
		'location': location
	}

@frappe.whitelist(allow_guest=True)
def check_subdomain_availability(subdomain):
	signup_domain = frappe.db.get_single_value('Central Settings', 'signup_domain') or frappe.local.conf.domain
	try:
		return validate_subdomain(subdomain)
	except frappe.DuplicateEntryError:
		frappe.local.message_log = []
		return '{0}.{1}'.format(subdomain, signup_domain)

