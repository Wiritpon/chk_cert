# Copyright (c) 2025, Zezembly and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ManufacturingLot(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		city_of_origin: DF.Data | None
		expiry_date: DF.Date | None
		harvesting_period: DF.Data | None
		lot_number: DF.Int
		manufacturing_date: DF.Date | None
		product: DF.Link
	# end: auto-generated types

	pass
