# -*- coding: utf-8 -*-
# Copyright (c) 2018, DPI and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe 
from frappe import _ 
from frappe.model.document import Document

class Meeting(Document):
	def validate(self):
		"""Set missing names and warn if duplicate"""
		found = []
		for attendees in self.attendees:
			if not attendees.full_name:
				attendees.full_name = get_full_name(attendees.attendees)

			if attendees.attendees in found:
				frappe.throw(_("Attendee {0} entered twice").format(attendees.attendees))

			found.append(attendees.attendees)	

@frappe.whitelist()
def get_full_name(attendees):
	print("\n\nin get full name")
	print(attendees)
	user = frappe.get_doc("User", attendees)
	print(user.email)
	return " ".join(filter(None, [user.first_name, user.middle_name, user.last_name]))

