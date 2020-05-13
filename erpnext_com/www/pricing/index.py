# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import frappe
import requests
from frappe.utils import fmt_money

eu = ["BE", "BG", "CZ", "DK", "DE", "EE", "IE", "EL", "ES", "FR", "HR",
	"IT", "CY", "LV", "LT", "LU", "HU", "MT", "NL", "AT", "PL", "PT",
	"RO", "SI", "SK", "FI", "SE"]

def get_context(context):
	context.no_cache = True
	country_details = frappe._dict(get_country())

	if country_details.countryCode == 'IN':
		context.currency = 'INR'
		context.symbol = '₹'

	else:
		context.currency = 'USD'
		context.symbol = '$'

	context.base_features = {
		'all_modules': {
			'title': 'All Modules',
			'content': 'Accounting, Inventory, HR and more'
		},
		'email_support': {
			'title': 'Standard Support',
			'content': 'Standard support during business hours'
		},
		'backup': {
			'title': 'Backup + Redundancy',
			'content': 'Daily offsite backups on AWS'
		},
		'priority_support': {
			'title': 'Priority Support',
			'content': 'High priority support with shorter SLA'
		},
		'hosting' : {
			'title': 'Hosting Included',
			'content': 'Managed hosting on our servers.'
		},
		'account_manager': {
			'title': 'Account Manager',
			'content': 'Dedicated account manager to fulfill your requirements.'
		},
		'onboarding_three':  {
			'title': '3 Hrs Onboarding Support'
		},
		'onboarding_5':  {
			'title': '5 Hrs Onboarding Support'
		},
		'onboarding':  {
			'title': 'Enterprise Onboarding'
		}
	}

	context.plan_features = ['Server and Emails', 'Customization', 'Integrations + API']

	pricing_multiplier_doc = frappe.get_doc({
			"doctype": "Pricing Multiplier"
		})

	pricing_multiplier = pricing_multiplier_doc.get_pricing_multiplier_details(country_details.country)

	def get_plan_and_pricing(plan_name):
		plan = frappe.get_doc('Base Plan', plan_name)
		_pricing_multiplier = 1
		pricing = [d.as_dict() for d in plan.amounts if d.currency == context.currency][0]

		if plan.apply_pricing_multiplier:
			_pricing_multiplier = pricing_multiplier

		pricing['monthly_amount'] = get_rounded_total((pricing['monthly_amount'] / plan.users), _pricing_multiplier)
		pricing['amount'] = get_rounded_total((pricing['amount'] / plan.users), _pricing_multiplier)
		pricing['symbol'] = context.symbol

		return plan, pricing

	business_plan, business_plan_pricing = get_plan_and_pricing('P-Standard-2020')
	enterprise_plan, enterprise_plan_pricing = get_plan_and_pricing('P-Pro-2020')

	context.plans = [
		{
			'name': business_plan.name,
			'title': business_plan.title,
			'pricing': business_plan_pricing,
			'storage': business_plan.space,
			'emails': business_plan.emails,
			'minimum_users': 5,
			'base_features': [
				{'title': 'hosting', 'included': 1},
				{'title': 'account_manager', 'included': 0},
				{'title': 'all_modules', 'included': 1},
				{'title': 'email_support', 'included': 1},
				{'title': 'onboarding_three', 'included': 1}
			],
			'features': [
				{
					'title': 'Organizations',
					'content': [
						'3 Companies',
					]
				},
				{
					'title': 'Server and Emails ',
					'content': [
						'10 GB cloud storage',
						'5000 emails / month',
						'Extensible via add-ons'
					]
				},
				{
					'title': 'Customization',
					'content': [
						'Print Formats and Email Alerts',
						'30 Custom Fields',
						'10 Custom Forms, 10 Custom Scripts'
					]
				},
				{
					'title': 'Integrations + API',
					'content': [
						'Email Integration and REST API',
						'Payment Gateways',
						'Dropbox, Shopify and AWS'
					]
				}
			],

		},
		{
			'name': enterprise_plan.name,
			'title': enterprise_plan.title,
			'pricing': enterprise_plan_pricing,
			'storage': enterprise_plan.space,
			'emails': enterprise_plan.emails,
			'minimum_users': 10,
			'base_features': [
				{'title': 'hosting', 'included': 1},
				{'title': 'account_manager', 'included': 0},
				{'title': 'all_modules', 'included': 1},
				{'title': 'email_support', 'included': 1},
				{'title': 'onboarding_5', 'included': 1}
			],
			'features': [
				{
					'title': 'Organizations',
					'content': [
						'Unlimited Companies',
					]
				},
				{
					'title': 'Server and Emails',
					'content': [
						'25 GB cloud storage',
						'15000 emails / month',
						'Extensible via add-ons'
					]
				},
				{
					'title': 'Customization',
					'content': [
						'Print Formats and Email Alerts',
						'Unlimited Custom Fields',
						'Unlimited Custom Forms and Scripts'
					]
				},
				{
					'title': 'Integrations + API',
					'content': [
						'Email Integration and REST API',
						'Payment Gateways',
						'Dropbox, Shopify and AWS'
					]
				}
			],
		},
		{
			'name': 'Contact Us',
			'title': 'Self Hosted',
			'no_pricing': True,
			'description': 'One Stack, One Vendor, 100% Freedom',
			'base_features': [
				{'title': 'hosting', 'included': 0},
				{'title': 'account_manager', 'included': 1},
				{'title': 'all_modules', 'included': 1},
				{'title': 'priority_support', 'included': 1},
				{'title': 'onboarding', 'included': 1}
			],
			'minimum_users': 100,
			'features': [
				{
					'title': 'Organizations',
					'content': [
						'Unlimited Companies',
					]
				},
				{
					'title': 'Server and Emails',
					'content': [
						'Private Server',
						'Unlimited storage',
						'Unlimited emails'
					]
				},
				{
					'title': 'Customization',
					'content': [
						'Print Formats and Email Alerts',
						'Unlimited Custom Fields',
						'Unlimited Custom Forms and Scripts'
					]
				},
				{
					'title': 'Integrations + API',
					'content': [
						'Email Integration and REST API',
						'Payment Gateways',
						'Dropbox, Shopify and AWS'
					]
				}
			],
		}
	]


@frappe.whitelist(allow_guest=True)
def get_plan_details(plan_name):
	plan_name = frappe.utils.escape_html(plan_name)
	currency = 'USD'
	symbol = '$'

	if get_country().get('countryCode') == 'IN':
		currency = 'INR'
		symbol = '₹'

	plan = frappe.get_doc('Base Plan', plan_name)
	pricing = [d for d in plan.amounts if d.currency == currency][0].as_dict()

	pricing['symbol'] = symbol

	plan = plan.as_dict()
	plan['pricing'] = pricing

	return plan

country_info = {}

@frappe.whitelist(allow_guest=True)
def get_country(fields=None):
	global country_info
	ip = frappe.local.request_ip

	if not ip in country_info:
		fields = ['countryCode', 'country', 'regionName', 'city']
		res = requests.get('https://pro.ip-api.com/json/{ip}?key={key}&fields={fields}'.format(
			ip=ip, key=frappe.conf.get('ip-api-key'), fields=','.join(fields)))

		try:
			country_info[ip] = res.json()

		except Exception:
			country_info[ip] = {}

	return country_info[ip]


def get_rounded_total(amount, pricing_multiplier):
	''' Python - round up to the nearest ten '''

	if pricing_multiplier != 1:
		amount = amount * pricing_multiplier
		return int(round(amount / 10.0)) * 10
	else:
		return amount