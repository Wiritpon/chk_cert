# Copyright (c) 2025, Zezembly and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class TestIndicator(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		category: DF.Data | None
		frequency: DF.Int
		indicator: DF.Data | None
		reference_standard: DF.Data | None
		specifications: DF.Data | None
		test_method: DF.Data | None
	# end: auto-generated types

	pass
