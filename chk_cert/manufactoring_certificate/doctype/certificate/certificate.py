# Copyright (c) 2025, Zezembly and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Certificate(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from chk_cert.manufactoring_certificate.doctype.test_result.test_result import TestResult
		from frappe.types import DF

		approved_by: DF.Data | None
		approved_position: DF.Data | None
		certificate_id: DF.Data
		certificate_type: DF.Data | None
		employee: DF.Link
		expiry_date: DF.Date | None
		issue_date: DF.Date | None
		lot: DF.Link
		recommended_storage: DF.Text | None
		remark: DF.Text | None
		table_pmpo: DF.Table[TestResult]
	# end: auto-generated types

	pass
