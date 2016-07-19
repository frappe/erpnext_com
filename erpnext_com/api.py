import frappe

from razorpay_integration.api import get_razorpay_checkout_url

# TODO:
# 1. send email to particpant and us
# 2. who is coming page
# 3. final design

@frappe.whitelist(allow_guest=True)
def make_payment(full_name, email, company, workshop=0, conference=0):
	amount = int(workshop or 0) * 2000 + int(conference or 0) * 600

	if not amount:
		frappe.msgprint('Please set no of tickets')
		return

	participant = frappe.get_doc({
		'doctype': 'Conference Participant',
		'full_name': full_name,
		'email_id': email,
		'company_name': company,
		'workshop': workshop,
		'conference': conference,
		'amount': amount
	}).insert(ignore_permissions=True)

	url = get_razorpay_checkout_url(**{
		'amount': amount,
		'title': 'ERPNext Conference Tickets',
		'description': '{0} passes for conference, {1} passes for workshop'.format(int(conference or 0), int(workshop or 0)),
		'payer_name': full_name,
		'payer_email': email,
		'doctype': participant.doctype,
		'name': participant.name,
		'order_id': participant.name
	})

	return url
