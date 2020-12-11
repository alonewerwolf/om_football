# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Footballer(models.Model):
    # _name = 'om_football.footballer'
    _description = 'Footballer Record'
    _inherit = 'account.analytic.line'

    footballer_name = fields.Char(string='Footballer Name', required=True)
    is_footballer = fields.Boolean(string='Is Footballer')
    footballer_age = fields.Integer('Age')
    footballer_number = fields.Integer('Number')
    # gender = fields.Selection([
    #     ('male', 'Male'),
    #     ('fe_male', 'Female')
    # ], default='male', string='Gender')
    description = fields.Text(string='Description')
    image = fields.Binary(string='Image')
    footballer_id = fields.Many2one('res.users', string="Responsible")

class Football_Club(models.Model):
    # _name = 'om_football.football_club'
    _inherit = 'account.analytic.line'
    football_club = fields.Char(string="FC", required=True)
    image = fields.Binary(string='Image')
    description = fields.Text()
    # fc_id = fields.One2many('om_fotball.footballer', 'footballer_id')