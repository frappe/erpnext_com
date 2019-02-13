from __future__ import unicode_literals
import frappe


no_cache = True

def get_context(context):
	references = frappe.get_all("CVE",
				    fields=["commit_url", "reference", "reporter_url", "reported_by", "affected_applications", "severity"],
				    filters=[['reported_on', '<', frappe.utils.add_months(frappe.utils.nowdate(), -2)]])
	return {"references": references}
