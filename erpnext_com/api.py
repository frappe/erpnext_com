import frappe

from razorpay_integration.templates.pages.razorpay_checkout import get_checkout_url as get_razorpay_checkout_url

@frappe.whitelist(allow_guest=True)
def make_payment(full_name, email, company, workshop=None, conference=None):
	participant = frappe.get_doc({
		'doctype': 'Conference Participant',
		'full_name': full_name,
		'email_id': email,
		'company_name': company,
		'workshop': workshop,
		'conference': conference
	}).insert()


	url = get_razorpay_checkout_url(**{
		'amount': int(workshop) * 2000 + int(conference) * 600,
		'title': 'ERPNext Conference Tickets',
		'description': '{0} passes for conference, {1} passes for workshop'.format(int(conference), int(workshop)),
		'payer_name': full_name,
		'payer_email': email,
		'doctype': participant.doctype,
		'name': participant.name,
		'order_id': participant.name
	})

	return url
