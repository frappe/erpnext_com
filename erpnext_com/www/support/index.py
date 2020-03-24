# -*- coding: utf-8 -*-

from erpnext_com.erpnext_com.utils import get_country

def get_context(context):
	context.no_cache = True
	country_code = get_country().get("countryCode")

	if country_code == 'IN':
		context.symbol = '₹'
		context.amount = '7000'

	else:
		context.symbol = '$'
		context.amount = '150'
