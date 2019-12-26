# -*- coding: utf-8 -*-

import frappe

eu = ["BE", "BG", "CZ", "DK", "DE", "EE", "IE", "EL", "ES", "FR", "HR",
	"IT", "CY", "LV", "LT", "LU", "HU", "MT", "NL", "AT", "PL", "PT",
	"RO", "SI", "SK", "FI", "SE"]

country_info = {}

@frappe.whitelist(allow_guest=True)
def get_country(fields=None):
	global country_info
	ip = frappe.local.request_ip

	if not ip in country_info:
		fields = ['countryCode', 'country', 'regionName', 'city']
		try:
			res = requests.get('https://pro.ip-api.com/json/{ip}?key={key}&fields={fields}'.format(
				ip=ip, key=frappe.conf.get('ip-api-key'), fields=','.join(fields)))

			country_info[ip] = res.json()

		except Exception:
			country_info[ip] = {}

	return country_info[ip]


