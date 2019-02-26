# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import frappe
import requests
from frappe import _
from central.signup import signup as _signup, validate_subdomain
from frappe.integrations.utils import get_checkout_url
from frappe.utils.momentjs import get_all_timezones

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