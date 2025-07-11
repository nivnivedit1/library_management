
# Copyright (c) 2025, Nivedita and contributors
# For license information, please see license.txt
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus
import frappe

class LibraryMembership(Document):
    def before_submit(self):
        exists = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": DocStatus.submitted(),
                "to_date": (">", self.from_date),
            },
        )
        if exists:
            frappe.throw("There is an active membership for this member")
