# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "erpnext_com"
app_title = "ERPNext.com"
app_publisher = "Frappe"
app_description = "ERPNext.com website"
app_icon = "fa fa-globe"
app_color = "black"
app_email = "info@erpnext.com"
app_url = "https://erpnext.com"
app_version = "0.0.1"
hide_in_installer = True

website_context = {
	"repo": "frappe/erpnext_com",
	"logo_image_url": '/assets/erpnext_com/img/erpnext-logo-blue.svg',
	'brand_name': 'ERPNext',
	"brand_html": "ERPNext",
	"top_bar_items": [
		{"label": "Solutions", "child_items": [
			{"label": "Services", "url":"/services"},
			{"label": "Manufacturing", "url":"/manufacturing"},
			{"label": "Retail", "url":"/retail"},
			{"label": "Distribution", "url":"/distribution"},
			{"label": "Education", "url":"/education"},
			{"label": "Non Profit", "url":"/non-profit"},
			{"label": "Agriculture", "url":"/agriculture"},
			{"label": "Healthcare", "url": "/healthcare"},
		]},
		{"label": "Cloud", "url": "/pricing"},
		{"label": "Services", "child_items": [
			{"label": "Support", "url": "/support"},
			{"label": "Enterprise", "url": "/enterprise"},
			{"label": "Contact Sales", "url": "/contact-form"},
		]},
		{"label": "Partners", "child_items": [
			{"label": "Partner Listing", "url":"/partners"},
			{"label": "Become a Partner", "url":"/partners/plans"},
		]},
		{"label": "Docs", "url": "/docs/user/manual/en", "right":1},
		{"label": "About", "url": "/about", "right":1},
	],
	"hide_login": 1,
	"favicon": "/assets/erpnext_com/img/erpnext-logo-blue.png"
}

website_redirects = [
	{'source': '/compare', 'target': 'https://erpnext.org/contribute' },
	{'source': '/benefits', 'target': '/about' },
	{'source': '/download', 'target': 'https://erpnext.org/get-started' },
	{'source': '/faq', 'target': 'https://erpnext.org/faq' },
	{'source': '/open-source', 'target': 'https://erpnext.org/open-source' },
]

look_for_sidebar_json = True

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_com/css/erpnext_com.css"
# app_include_js = "/assets/erpnext_com/js/erpnext_com.js"

# include js, css files in header of web template
web_include_css = "/assets/erpnext_com/css/custom.css"
web_include_js = "/assets/erpnext_com/js/payment.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "index"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_com.install.before_install"
# after_install = "erpnext_com.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_com.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnext_com.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_com.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_com.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_com.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_com.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnext_com.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_com.event.get_events"
# }

fixtures = ["Contact Us Settings"]
