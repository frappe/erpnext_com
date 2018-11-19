from __future__ import unicode_literals
import frappe
from central.utils import get_signup_domain
from central.signup import is_payment_mandatory
no_cache = True

def get_context(context):
	return {
		'signup_domain': get_signup_domain() or 'erpnext.com',
		'is_payment_mandatory': is_payment_mandatory
	}
