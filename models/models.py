# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.base.models.res_partner import _tz_get

class Footballer(models.Model):
    # _name = 'om_football.footballer'
    _description = 'Footballer Record'
    _inherit = 'account.analytic.line'

    @api.depends('footballer_age')
    def _compute_age_group(self):
        for rec in self:
            if rec.footballer_age:
                if rec.footballer_age < 20:
                    rec.age_group = 'minor'
                else:
                    rec.age_group = 'major'

    footballer_name = fields.Char(string='Footballer Name', required=True)
    is_footballer = fields.Boolean(string='Is Footballer')
    footballer_age = fields.Integer('Age')
    age_group = fields.Selection([
        ('major', 'Major'),
        ('minor', 'Minor'),
    ], string="Age Group", compute='_compute_age_group')
    footballer_number = fields.Integer('Number')
    description = fields.Text(string='Description')
    image = fields.Binary(string='Image')
    footballer_id = fields.Many2one('res.users', string="Responsible", default=lambda self: self.env.user)

class Football_Club(models.Model):
    # _name = 'om_football.football_club'
    _inherit = 'account.analytic.line'
    tz = fields.Selection(_tz_get, string='Timezone', required=True,
                          default=lambda self: self.env.user.tz or 'UTC')
    football_club = fields.Char(string="FC", required=True)
    created_date = fields.Date(default=fields.Date.today)
    image = fields.Binary(string='Image')
    description = fields.Text()
    fc_id = fields.One2many('football.acs', 'user_id')

