from __future__ import unicode_literals
import frappe
from frappe.utils import cint

def get_context(context):
	plan_details = []
	for plan in frappe.db.sql('''
		select bp.name, bp.users, bp.space, bp.emails, bpa.amount
				from `tabBase Plan` bp
				left join `tabPlan Amount` bpa
					on (bpa.parent = bp.name and bpa.currency="USD")
				where bp.is_an_upgrade=1 order by bpa.amount asc
	''', as_dict=1):
		plan['amount'] = cint(plan['amount'])
		plan['space'] = cint(plan['space'])
		plan_details.append(plan)

	return {
		"plan_details": plan_details
	}