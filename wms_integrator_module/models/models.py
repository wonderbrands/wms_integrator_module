# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CarrierSelector(model.model):
    _name = "carriers.list"

    name = fields.Char(
        string = "Carrier Name"
    )

    code = fields.Char(
        string = "Carrier internal code",
        index = True
    )

    full_name = fields.Float(compute='_compute_name')

    @api.depends('name', 'code')
    def _compute_name(self):
        for record in self:
            record.total = f"{record.code} {record.name}"

    @api.model
    def name_get(self):
        result = []
        for record in self:
            display_name = record.full_name
            result.append((record.id, display_name))
        return result




class wmsFields(models.Model):
    _inherit = 'sale.order'
    _description = 'WMS fields'

    carrier_selection_relational = fields.Many2one(
        name = "Select carrier",
        comodel_name = "carriers.list",
        options={
            'no_create': True
        }
    )

    select_carrier = fields.Selection([
            ('FDX', 'FedEx'),
            ('EST', 'Estafeta'),
            ('DHL', 'DHL'),
            ('PQX', 'PaquetExpress'),
            ('UPS', 'UPS'),
            ('99M', '99 mins'),
            ('SEGM', 'Segmail'),
            ('PCKM', 'Packmail'),
            ('CWM', 'Colecta Walmart'),
            ('CMEL', 'Colecta MELI'),
            ('CAMZ', 'Colecta Amazon'),
            ('RBY', 'Rapiboy'),
            ('CNV', 'Casanova'),
            ('CNX', 'Conexión'),
            ('TGR', 'Tres Guerras'),
            ('CCPL', 'Colecta Coopel'),
            ('AMPM', 'AMPM'),
            ('IML', 'iMile'),
            ('JTE', 'J&TExpress'),
            ('YLT', 'Yaltec')
        ],string="Paquetería o Carrier")

    wms_status = fields.Selection([
            ('PNFF', 'Pendiente'),
            ('PREP', 'Preparado'),
            ('DESP', 'Despachado'),
            ('PNFS', 'Frenada (Sin Stock)'),
            ('PNFD', 'Frenada (Incompleta en OMS)'),
            ('PNFE', 'Frenada (Sin Etiqueta)'),
            ('PNPP', 'Frenada (Por Procesar)'),
            ('CANC', 'Cancelado'),
            ('ARCH', 'Archivada')
        ],string="Estado WMS")