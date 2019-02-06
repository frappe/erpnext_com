from __future__ import unicode_literals
import frappe


no_cache = True

def get_context(context):
	references = frappe.get_all("CVE", fields="*")
	return {"references": references}
