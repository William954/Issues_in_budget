# -*- coding: utf-8 -*-

from odoo import api, _, tools, fields, models, exceptions, SUPERUSER_ID
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
from datetime import datetime, date, time

class TablaPresupuesto(models.Model):
    _inherit = "crossovered.budget.lines"

    variacion_presupuesto = fields.Monetary(string="Variación vs Presupuesto",compute="variation")

    @api.one
    @api.depends("planned_amount","practical_amount")
    def variation(self):
        self.variacion_presupuesto = self.planned_amount - self.practical_amount
