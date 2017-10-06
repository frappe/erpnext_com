from __future__ import unicode_literals
import frappe
from frappe.utils import cint
from frappe.sessions import get_geo_ip_country

def get_context(context):
	plan_details = []
	currency_condition = get_user_currency()

	for plan in frappe.db.sql('''
		select bp.name, bp.users, bp.space, bp.emails, bpa.amount
				from `tabBase Plan` bp
				left join `tabPlan Amount` bpa
					on (bpa.parent = bp.name and bpa.currency="{currency}")
				where bp.is_an_upgrade=1 order by bpa.amount asc
	'''.format(**currency_condition), as_dict=1):
		plan['amount'] = cint(plan['amount'])
		plan['space'] = cint(plan['space'])
		plan.update(currency_condition)
		plan_details.append(plan)

	return {
		"plan_details": plan_details
	}

def get_user_currency():
	conditions = dict(currency="USD")
	country_code = get_geo_ip_country(frappe.local.request_ip) if frappe.local.request_ip else None

	if country_code == 'IN':
		conditions.update(dict(currency="INR"))

	return conditions