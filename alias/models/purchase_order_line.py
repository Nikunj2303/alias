# purchase_order_line.py

from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    alias_id = fields.Many2one('alias.ids', string='Alias', index=True)

    @api.onchange('alias_id')
    def onchange_alias_id(self):
        if self.alias_id:
            product = self.env['product.template'].search([('alias_ids', '=', self.alias_id.id)], limit=1)
            if product:
                self.product_id = product.id
