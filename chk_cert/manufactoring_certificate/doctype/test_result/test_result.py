# Copyright (c) 2025, Zezembly and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class TestResult(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		category: DF.Link | None
		certificate_id: DF.Link | None
		frequency: DF.Link | None
		indicator: DF.Link | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		reference_standard: DF.Link | None
		result: DF.Data | None
		result_value: DF.Data | None
		specifications: DF.Link | None
		test_method: DF.Link | None
		tested_by: DF.Data | None
		tested_date: DF.Date | None
	# end: auto-generated types

	pass
