# Copyright (c) 2025, Zezembly and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ProductTestSpecification(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		indicator_id: DF.Int
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		product: DF.Link
		specification_value: DF.Data | None
	# end: auto-generated types

	pass
