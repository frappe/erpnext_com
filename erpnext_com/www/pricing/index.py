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
	country_code = get_country().get("countryCode")

	if country_code == 'IN':
		context.currency = 'INR'
		context.symbol = '₹'

	else:
		context.currency = 'USD'
		context.symbol = '$'

	context.base_features = {
		'all_modules': {
			'title': 'All Modules',
			'content': 'Accounting, Inventory, HR and more',
			'bold': False
		},
		'email_support': {
			'title': 'Email Support',
			'content': 'Email Support during bussiness hours',
			'bold': False
		},
		'backup': {
			'title': 'Backup + Redundancy',
			'content': 'Daily offsite backups on AWS',
			'bold': False
		},
		'priority_support': {
			'title': 'Priority Support',
			'content': 'High priority support with shorter SLA',
			'bold': False
		},
		'account_manager': {
			'title': 'Account Manager',
			'content': 'Dedicated account manager to fulfill your requirements.',
			'bold': True
		}
	}

	context.plan_features = ['Server and Emails', 'Customization', 'Integrations + API']

	def get_plan_and_pricing(plan_name):
		plan = frappe.get_doc('Base Plan', plan_name)
		pricing = [d.as_dict() for d in plan.amounts if d.currency == context.currency][0]
		pricing['monthly_amount'] = pricing['monthly_amount'] / plan.users
		pricing['amount'] = pricing['amount'] / plan.users
		pricing['symbol'] = context.symbol

		return plan, pricing

	business_plan, business_plan_pricing = get_plan_and_pricing('P-Standard-2019')
	enterprise_plan, enterprise_plan_pricing = get_plan_and_pricing('P-Pro-2019')

	context.plans = [
		{
			'name': business_plan.name,
			'title': business_plan.title,
			'pricing': business_plan_pricing,
			'storage': business_plan.space,
			'emails': business_plan.emails,
			'minimum_users': 5,
			'base_features': ['all_modules', 'email_support', 'backup'],
			'features': [
				{
					'title': 'Organisations',
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
			'minimum_users': 5,
			'base_features': ['account_manager', 'all_modules', 'priority_support', 'backup'],
			'features': [
				{
					'title': 'Organisations',
					'content': [
						'Unlimited Companies',
					]
				},
				{
					'title': 'Server and Emails',
					'content': [
						'15 GB cloud storage',
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
			'title': 'Enterprise',
			'no_pricing': True,
			'description': 'Starts at ' + ("$150" if context.currency == "USD" else "₹7000") + ' per user per year',
			'base_features': ['account_manager', 'all_modules', 'priority_support', 'backup'],
			'minimum_users': 20,
			'features': [
				{
					'title': 'Organisations',
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
