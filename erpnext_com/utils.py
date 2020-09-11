# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import frappe
import requests

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
