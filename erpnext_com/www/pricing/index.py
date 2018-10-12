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
	country = get_country()
	country = country

	if country == 'IN':
		context.currency = 'INR'
		context.symbol = '₹'

	else:
		context.currency = 'USD'
		context.symbol = '$'

	context.base_features = [
		{
			'title': 'All Modules',
			'content': 'Unlimited features with Accounting, Inventory, HR and Payroll'
		},
		{
			'title': 'Personalized Support',
			'content': 'In app priority support from the team that brought you ERPNext'
		},
		{
			'title': 'Backup + Redundancy',
			'content': 'Servers with offsite snapshot backups ensuring max reliability'
		}
	]

	context.plan_features = ['Server and Emails', 'Customization', 'Integrations + API']

	def get_plan_and_pricing(plan_name):
		plan = frappe.get_doc('Base Plan', plan_name)
		pricing = [d.as_dict() for d in plan.amounts if d.currency == context.currency][0]
		pricing['symbol'] = context.symbol

		return plan, pricing

	basic_plan, basic_plan_pricing = get_plan_and_pricing('P-Basic')
	business_plan, business_plan_pricing = get_plan_and_pricing('P-Business')
	enterprise_plan, enterprise_plan_pricing = get_plan_and_pricing('P-Enterprise')

	context.plans = [
		{
			'name': basic_plan.name,
			'title': 'Basic',
			'pricing': basic_plan_pricing,
			'storage': basic_plan.space,
			'emails': basic_plan.emails,
			'features': [
				{
					'title': context.plan_features[0],
					'content': [
						'2 GB cloud storage',
						'2000 emails / month',
						'Extensible via add-ons'
					]
				},
				{
					'title': context.plan_features[1],
					'content': [
						'Customized Print Formats and Email Alerts',
						'10 Custom Fields',
						'1 Custom Form'
					]
				},
				{
					'title': context.plan_features[2],
					'content': [
						'Integrations with Email and REST API'
					]
				}
			],

		},
		{
			'name': business_plan.name,
			'title': 'Business',
			'pricing': business_plan_pricing,
			'storage': business_plan.space,
			'emails': business_plan.emails,
			'features': [
				{
					'title': context.plan_features[0],
					'content': [
						'5 GB cloud storage',
						'5000 emails / month',
						'Extensible via add-ons'
					]
				},
				{
					'title': context.plan_features[1],
					'content': [
						'Customized Print Formats and Email Alerts',
						'Unlimited Custom Fields',
						'10 Custom Forms, 10 Custom Scripts'
					]
				},
				{
					'title': context.plan_features[2],
					'content': [
						'Integrations with Email and REST API',
						'Dropbox, Shopify and AWS'
					]
				}
			],

		},
		{
			'name': enterprise_plan.name,
			'title': 'Enterprise',
			'pricing': enterprise_plan_pricing,
			'storage': enterprise_plan.space,
			'emails': enterprise_plan.emails,
			'features': [
				{
					'title': context.plan_features[0],
					'content': [
						'15 GB cloud storage',
						'15000 emails / month',
						'Extensible via add-ons'
					]
				},
				{
					'title': context.plan_features[1],
					'content': [
						'Customized Print Formats and Email Alerts',
						'Unlimited Custom Fields, Forms and Scripts',
						'1 Custom App Installation'
					]
				},
				{
					'title': context.plan_features[2],
					'content': [
						'Integrations with Email and REST API',
						'Dropbox, Shopify and AWS'
					]
				}
			],

		}
	]

@frappe.whitelist(allow_guest=True)
def get_country():
	ip = frappe.local.request_ip

	res = requests.get('https://pro.ip-api.com/json/{ip}?key={key}&fields=countryCode'.format(
		ip=ip, key=frappe.conf.get('ip-api-key')))

	try:
		country_code = res.json().get('countryCode')
		return country_code

	except Exception:
		return ''
