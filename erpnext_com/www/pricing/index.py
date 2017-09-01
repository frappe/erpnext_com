from __future__ import unicode_literals
import frappe

def get_context(context):
	plan_details = frappe.db.sql('''
		select bp.name, bp.users, bp.space, bp.emails, bpa.amount
				from `tabBase Plan` bp
				left join `tabPlan Amount` bpa
					on (bpa.parent = bp.name and bpa.currency="USD")
				where bp.is_an_upgrade=1 order by bpa.amount asc
	''', as_dict=1)

	return {
		"plan_details": plan_details
	}