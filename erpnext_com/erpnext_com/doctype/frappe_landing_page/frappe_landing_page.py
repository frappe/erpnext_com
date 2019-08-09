# -*- coding: utf-8 -*-
# Copyright (c) 2019, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document

class FrappeLandingPage(WebsiteGenerator):
	website = frappe._dict(
		page_title_field="title",
		condition_field="is_published",
		template="erpnext_com/doctype/frappe_landing_page/templates/landing_page.html",
		no_cache=1
	)

	def get_context(self, context):
		context.website = self
