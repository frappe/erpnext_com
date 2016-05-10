import frappe

def get_context(context):
    context.no_cache = True
    context.update(frappe.get_doc('ERPNext Domain', frappe.form_dict.name).as_dict())
