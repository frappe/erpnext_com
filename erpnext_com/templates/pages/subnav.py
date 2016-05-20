import frappe

def get_context(context):
    context.no_cache = True
    context.update(frappe.get_doc('Subsite', frappe.form_dict.name).as_dict())
print frappe.get_doc('Subsite', frappe.form_dict.name).as_dict()