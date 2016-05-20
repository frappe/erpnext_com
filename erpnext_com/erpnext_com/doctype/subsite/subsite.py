# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Subsite(Document):
	pass

# def get_context(context):
# 	context = frappe._dict({
# 		'subnav_bar_items': get_items('subnav_bar_items'),
# 	})
# 	return context
#
# def get_items(parentfield):
# 	all_subnav_items = frappe.db.sql("""\
# 		select * from `tabSub Navbar Item`
# 		where parent='Subsite' and parentfield= %s
# 		order by idx asc""", parentfield, as_dict=1)
#
# 	subnav_items = [d for d in all_subnav_items if not d['parent_label']]
#
# 	# attach child items to the bar
# 	for d in all_subnav_items:
# 		if d['parent_label']:
# 			for t in subnav_items:
# 				if t['label']==d['parent_label']:
# 					if not 'child_items' in t:
# 						t['child_items'] = []
# 					t['child_items'].append(d)
# 					break
# 	return subnav_items
