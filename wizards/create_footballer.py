from odoo import fields, models, api


class CreateFootballer(models.TransientModel):
    _name = 'create.footballer'
    _description = 'Wizard'

    def _default_session(self):
        return self.env['account.analytic.line'].browse(
            self._context.get('active_id'))

    footballer_id = fields.Many2one('account.analytic.line', string='Footballer')
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    
