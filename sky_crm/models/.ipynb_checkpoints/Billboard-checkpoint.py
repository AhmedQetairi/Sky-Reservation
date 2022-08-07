from odoo import api, fields, models
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError


class SkyBillboard(models.Model):
    _name = "sky.billboard"
    _description = "Sky Billboard"

    name = fields.Char(string='Billboard Name', required=True, translate=True)
    include_initial_balance = fields.Boolean(string="")
    type = fields.Selection([
        ('occupied', 'Occupied'),
        ('available', 'Available'),
    ], required=True, default='available')