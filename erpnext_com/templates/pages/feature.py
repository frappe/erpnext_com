# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe

def get_context(context):
    context.no_cache = True
    context.update(frappe.get_doc('ERPNext Feature', frappe.form_dict.name).as_dict())