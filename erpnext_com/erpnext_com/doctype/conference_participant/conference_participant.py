# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.model.document import Document

class ConferenceParticipant(Document):
	def on_payment_authorized(self):
		self.paid = 1
		self.save(ignore_permissions=True)
