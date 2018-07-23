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

	context.currency = 'USD'
	context.symbol = '$'
	context.rate = 150

	if context.country == 'IN':
		context.currency = 'INR'
		context.symbol = '₹'
		context.rate = 10000

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

	context.rate = fmt_money(context.rate)[:-3]


@frappe.whitelist(allow_guest=True)
def get_country():
	ip = '2405:201:23:fee6:18d4:2134:5d99:5dcc'
	#ip = frappe.local.request_ip
	country_code = requests.get('https://pro.ip-api.com/json/{ip}?key={key}&fields=countryCode'.format(
		ip=ip, key=frappe.conf.get('ip-api-key'))).json().get('countryCode')

	return country_code