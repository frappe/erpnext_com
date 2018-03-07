from __future__ import unicode_literals
import frappe
from frappe.utils import cint

def get_context(context):
	common_features = [
		"Priority Support",
		"Bug Fix Guarantee",
		"All Modules",
		"All Domains",
		"Auto-Upgrades",
		"Automated Backups",
		"Custom Domain"
	]

	start_features = [
		"10 Users",
		"10 GB Space",
		"10,000 Emails",
	]

	medium_features = [
		"100 Users",
		"100 GB Space",
		"100,000 Emails",
	]

	enterprise_features = [
		"Unlimited Users",
		"Unlimited Space",
		"Unlimited Emails",
	]
	enterprise_extras = [
	]
	plans = [
		{"name": "Small",
		"price": "$ 125<span class=\"small\">/month</span>",
		"info": "Billed Annually",
		"features": start_features + common_features
		},

		{"name": "Medium",
		"price": "$ 800<span class=\"small\">/month</span>",
		"info": "Billed Annually",
		"features": medium_features + common_features
		},
		{"name": "Enterprise",
		"price": "Custom",
		"info": "Dedicated",
		"features": enterprise_features + common_features
		}
	]
	return {"plans": plans}
