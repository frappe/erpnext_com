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

	medium_extras = [
		"5 Custom Print Formats",
		"5 Custom Reports"
		]

	enterprise_extras = [
		"Dedicated Engineer",
		"Custom Print Formats",
		"Custom Reports",
		"Feature Development"
		]

	plans = [
		{"name": "Small",
		"price": "$ 125<span class=\"small\">/month</span>",
		"info": "Billed Annually",
		"cta": "Start Trial",
		"ctalink": "onclick=\"redirect_to_signup('signup', 'P10-2018')\"",
		"features": start_features + common_features
		},

		{"name": "Medium",
		"price": "$ 800<span class=\"small\">/month</span>",
		"info": "Billed Annually",
		"cta": "Start Trial",
		"ctalink":  "onclick=\"redirect_to_signup('signup', 'P100-2018')\"",
		"features": medium_features + common_features + medium_extras
		},

		{"name": "Enterprise",
		"price": "Custom",
		"info": "Dedicated Server",
		"cta": "Contact Us",
		"ctalink": "onclick=\"window.location='https://frappe.io/about#contact'\";",
		"features": enterprise_features + common_features + enterprise_extras
		}
		]
	return {"plans": plans}
