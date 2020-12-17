# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from odoo.addons.base.models.res_partner import _tz_get




class Footballer(models.Model):
    # _name = 'om_football.footballer'
    _description = 'Footballer Record'
    _inherit = 'account.analytic.line'

    @api.depends('footballer_age')
    def _compute_age_group(self):
        for rec in self:
            rec.age_group = 'major'
            if rec.footballer_age:
                if rec.footballer_age < 20:
                    rec.age_group = 'minor'

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        for rec in self:
            return {'domain': {
                'order_id': [('partner_id', '=', rec.partner_id.id)]}}

    @api.model
    def default_get(self, fields_list=[]):
        print('field list', fields_list)
        rec = super(Footballer, self).default_get(fields_list)
        rec['active'] = True
        rec['footballer_name'] = "Ribery"
        # rec['footballer_id'] = self.env.user
        print(rec)
        return rec

    @api.constrains('partner_id', 'attendee_ids')
    def _check_partner_not_in_attendees(self):
        for rec in self:
            if rec.partner_id and rec.partner_id in rec.attendee_ids:
                raise exceptions.ValidationError(
                    "A session's partner can't be an attendee")

    def name_create(self, name):
        print("Name", name)
        res = self.create({'name': name})
        return res

    def write(self, values):
        print("Values", values)
        values['active'] = True
        rtn = super(Footballer, self).write(values)
        print("Return data", rtn)
        return rtn

    def action_confirm(self):
        footballers_age_major = self.env['account.analytic.line'].search(
            ['age_group' '=', 'major'])
        print('major footballers', footballers_age_major)
        footballers_age_minor = self.env['account.analytic.line'].search(
            ['age_group' '=', 'minor'])
        print('minor footballers', footballers_age_minor)

    @api.model
    def partners_by_country(self):
        sql = ('SELECT footballer_name '
               'FROM account.analytic.lines '
               'WHERE active=true')
        self.env.cr.execute(sql)
        record = self.env.cr.fetchall()
        print("Records:", record)



    footballer_name = fields.Char(string='Footballer Name', required=True)
    is_footballer = fields.Boolean(string='Is Footballer')
    footballer_age = fields.Integer('Age')
    age_group = fields.Selection(selection=[
        ('major', 'Major'),
        ('minor', 'Minor'),
    ], string="Age Group", default='major', compute='_compute_age_group')
    footballer_number = fields.Integer('Number')
    partner_id = fields.Many2one('res.partner', string='Customer')
    attendee_ids = fields.Many2many('res.partner', string='Attendees')
    order_id = fields.Many2one('sale.order', string='Sale Order')
    description = fields.Text(string='Description')
    image = fields.Binary(string='Image')
    footballer_id = fields.Many2one('res.users', string="Responsible")
    active = fields.Boolean(string="Active")


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

