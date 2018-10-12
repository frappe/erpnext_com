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
	context.country = get_country()

	if context.country == 'IN':
		context.currency = 'INR'
		context.symbol = '₹'
		context.rate = 1200

	elif context.country in eu:
		context.currency = 'EUR'
		context.symbol = '€'
		context.rate = 125

	elif context.country == 'UK':
		context.currency = 'GBP'
		context.symbol = '£'
		context.rate = 120

	elif context.country == 'AE':
		context.currency = 'AED'
		context.symbol = 'د.إ'
		context.rate = 550

	else:
		context.currency = 'USD'
		context.symbol = '$'
		context.rate = 19.99

	context.rate = fmt_money(context.rate)

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

	context.plans = [
		{
			'name': 'P-Basic',
			'title': 'Basic',
			'pricing': [
				{
					'currency': 'USD',
					'symbol': '$',
					'monthly_rate': 5,
					'annual_rate': 50
				},
				{
					'currency': 'INR',
					'symbol': '₹',
					'monthly_rate': 200,
					'annual_rate': 2000
				}
			],
			'storage': 2,
			'emails': 2000,
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
			'name': 'P-Business',
			'title': 'Business',
			'pricing': [
				{
					'currency': 'USD',
					'symbol': '$',
					'monthly_rate': 10,
					'annual_rate': 100
				},
				{
					'currency': 'INR',
					'symbol': '₹',
					'monthly_rate': 500,
					'annual_rate': 5000
				}
			],
			'storage': 5,
			'emails': 5000,
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
			'name': 'P-Enterprise',
			'title': 'Enterprise',
			'pricing': [
				{
					'currency': 'USD',
					'symbol': '$',
					'monthly_rate': 25,
					'annual_rate': 250
				},
				{
					'currency': 'INR',
					'symbol': '₹',
					'monthly_rate': 1500,
					'annual_rate': 15000
				}
			],
			'storage': 15,
			'emails': 15000,
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
