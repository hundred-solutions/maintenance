# Copyright 2022 Tecnativa - Víctor Martínez
# Copyright 2024 Tecnativa - Carolina Fernandez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Maintenance Product",
    "version": "17.0.1.0.0",
    "category": "Maintenance",
    "website": "https://github.com/OCA/maintenance",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": ["maintenance", "product"],
    "installable": True,
    "data": [
        "views/maintenance_equipment_view.xml",
        "views/product_template_view.xml",
    ],
    "maintainers": ["victoralmau"],
}
