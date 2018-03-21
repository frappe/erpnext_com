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
		"Custom Domain",
		"Mobile App"
		]

	start_features = [
		"5 Users",
		"<span class='bold'>Add User at $12.5/month</span>",
		"5 GB Space",
		"5,000 Emails"
		]

	medium_features = [
		"100 Users",
		"<span class='bold'>Add User at $12.5/month</span>",
		"100 GB Space",
		"100,000 Emails"
		]

	enterprise_features = [
		"Unlimited Users",
		"Unlimited Space",
		"Unlimited Emails"
		]

	medium_extras = [
		"5 Custom Reports",
		"5 Custom Print Formats"
		]

	enterprise_extras = [
		"Custom Reports",
		"Custom Print Formats",
		"Dedicated Engineer",
		"Feature Development"
		]

	plans = [
		{"name": "Small",
		"price": "$ 70<span class=\"small\">/month</span>",
		"info": "Billed Annually",
		"cta": "Start Trial",
		"ctalink": "onclick=\"redirect_to_signup('signup', 'P5-2018')\"",
		"features": start_features + common_features
		},

		{"name": "Medium",
		"price": "$ 800<span class='small'>/month</span>",
		"info": "Billed Annually",
		"cta": "Start Trial",
		"ctalink": "onclick=\"redirect_to_signup('signup', 'P100-2018')\"",
		"features": medium_features + common_features + medium_extras
		},

		{"name": "Enterprise",
		"price": "Custom",
		"info": "Dedicated Server",
		"cta": "Contact Us",
		"ctalink": "href='/contact'",
		"features": enterprise_features + common_features + enterprise_extras
		}
		]
	return {"plans": plans}
