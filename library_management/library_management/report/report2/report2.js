// Copyright (c) 2025, Nivedita and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["report2"] = {
	"filters": [
 {
      fieldname: "status",
      label: "Status",
      fieldtype: "Select",
      options: "\nAvailable\nIssued",
      default: "Available"
    }
	]
};
