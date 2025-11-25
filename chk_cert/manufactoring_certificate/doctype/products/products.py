# Copyright (c) 2025, Zezembly and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Products(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		description: DF.Text | None
		part_used: DF.Data | None
		plant_name: DF.Data | None
		product_id: DF.Int
		product_image: DF.AttachImage | None
		shelf_life: DF.Data | None
	# end: auto-generated types

	pass
