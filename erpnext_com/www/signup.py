from __future__ import unicode_literals
import frappe
from central.utils import get_signup_domain
no_cache = True

def get_context(context):
	return {
		'signup_domain': get_signup_domain() or 'erpnext.com'
	}
