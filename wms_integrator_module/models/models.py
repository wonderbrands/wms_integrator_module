# -*- coding: utf-8 -*-

from odoo import models, fields, api


class wmsFields(models.Model):
    _inherit = 'sale.order'
    _description = 'WMS fields'

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