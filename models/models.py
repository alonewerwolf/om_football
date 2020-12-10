# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Footballer(models.Model):
    # _name = 'om_football.footballer'
    # _description = 'Footballer Record'
    _inherit = 'account.analytic.line'

    name = fields.Char(string='Name', required=True)
    footballer_age = fields.Integer('Age')
    footballer_number = fields.Integer('Number')
    gender = fields.Selection([
        ('male', 'Male'),
        ('fe_male', 'Female')
    ], default='male', string='Gender')
    description = fields.Text(string='Description')
    image = fields.Binary(string='Image')
    footballer_id = fields.Many2one('my_module.football_club')

class Football_Club(models.Model):
    _inherit = 'account.analytic.line'

    football_club = fields.Char(string="FC", required=True)
    image = fields.Binary(string='Image')
    description = fields.Text()
    fc_id = fields.One2many('my_module.footballer', 'footballer_id')