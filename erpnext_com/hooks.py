# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "erpnext_com"
app_title = "ERPNext.com"
app_publisher = "Frappe"
app_description = "ERPNext.com website"
app_icon = "icon-globe"
app_color = "black"
app_email = "info@erpnext.com"
app_url = "https://erpnext.com"
app_version = "0.0.1"
hide_in_installer = True

website_context = {
	"brand_html": "ERPNext",
	"top_bar_items": [
		{"label": "Pricing", "url": "/pricing", "right":1},
		{"label": "Features", "url": "/features", "right":1},
		{"label": "Demo", "url": "https://demo.erpnext.com", "right":1},
		{"label": "Docs", "url": "https://manual.erpnext.com", "right":1},
		{"label": "Blog", "url": "https://blog.frappe.io", "right":1}
	],
	"hide_login": 1
}


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_com/css/erpnext_com.css"
# app_include_js = "/assets/erpnext_com/js/erpnext_com.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_com/css/erpnext_com.css"
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
