# -*- coding: utf-8 -*-
# Copyright (c) 2019, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import get_request_session

class CVEReportForm(Document):

	def after_insert(self):
		session = get_request_session()
		login(session)
		response = session.post('{host}/api/resource/Issue'.format(host=frappe.conf.api_host, data={
				"data": {
					json.dumps({
						"subject": "{name} [{severity}] {app} - {vulnerability}".format(
							name=self.name,
							severity=self.severity,
							app=self.affected_application,
							vulnerability=self.vulnerability_type
						),
						"status": "Open",
						"support_team": "Security",
						"issue_type": "Security Vulnerability",
						"raised_by": self.email_address,
						"description": self.vulnerability_description
				})}
			}))
		try:
			response.raise_for_status()
		except Exception:
			traceback = frappe.get_traceback()
			frappe.log_error(traceback)


def login(session):
	r = session.post('{host}/'.format(host=frappe.conf.api_host), data={
		'cmd': 'login',
		'usr': frappe.conf.api_username,
		'pwd': frappe.conf.api_password
	})

	try:
		if not r.json().get('message') == "Logged In":
			raise Exception
	except json.decoder.JSONDecodeError:
		raise Exception


def logout(session):
	session.get('{host}/?cmd=logout'.format(host=frappe.conf.api_host))
