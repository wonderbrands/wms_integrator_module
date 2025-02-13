from odoo import models, api, fields


class WMSStatusSP(models.Model):

    _name = "wms_integrator_module.stock_picking_status"

    name = fields.Char(
        string="Carrier Name",
        required=True,
        index=True
    )

    code = fields.Char(
        string="Carrier internal code",
        required=True
    )

    full_name = fields.Char(compute='_compute_name')

    @api.depends('name', 'code')
    def _compute_name(self):
        for record in self:
            record.full_name = f"{'' if not record.code else record.code} - {'' if not record.name else record.name}"


class StockPickingWMSInherit(models.Model):
    _inherit = "stock.picking"

    wms_status = fields.Many2one(
        name="Select carrier",
        comodel_name="wms_integrator_module.stock_picking_status",
        options={
            'no_create': True
        }
    )
