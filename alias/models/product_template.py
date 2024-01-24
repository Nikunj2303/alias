
from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    alias_ids = fields.One2many('product.template','alias_ids', string='Aliases')
