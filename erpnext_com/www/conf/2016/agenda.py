import frappe
import babel.dates
from frappe.utils import get_time

def get_context(context):
	context.get_formated_time = get_formated_time

def get_formated_time(time):
	return babel.dates.format_time(get_time(time), format='short', locale=(frappe.local.lang or "").replace("-", "_"))