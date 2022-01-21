# -*- coding: utf-8 -*-

from odoo import models, fields


class add_branch(models.Model):
    _inherit = 'res.partner'

    branch2 = fields.Char()
