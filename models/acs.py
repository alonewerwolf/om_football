
from odoo import models, fields

class Acs(models.Model):
    _name = 'football.acs'

    name = fields.Char(string="Name", required=True)
    user_id = fields.Many2one('res.users', sting='Responsible')