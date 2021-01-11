from odoo import fields, models, api


class FootballerName(models.Model):
    _inherit = 'account.analytic.line'
    _description = 'Description'

    footballer_name = fields.Char('Footballer Name', readonly=True)
    footballer_age = fields.Integer('Footballer Age', readonly=True)

    def _select(self):
        return super(FootballerName, self)._select() + """,
                t.footballer_name,
                t.footballer_age
                """

    def _group_by(self):
        return super(FootballerName, self)._group_by() + """,
                footballer_name,
                footballer_age
                """
