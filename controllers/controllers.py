# -*- coding: utf-8 -*-
from odoo import http

class Footballer(http.Controller):
    @http.route('/footballer/name/', website=True, auth='public')
    def footballer_names(self, **kw):
        name = http.request.env['account.analytic.line']
        return http.request.render('om_football.footballer_name', {
            'footballer': name.search([])
        })

# class OmFootball(http.Controller):
#     @http.route('/om_football/om_football/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_football/om_football/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_football.listing', {
#             'root': '/om_football/om_football',
#             'objects': http.request.env['om_football.om_football'].search([]),
#         })

#     @http.route('/om_football/om_football/objects/<model("om_football.om_football"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_football.object', {
#             'object': obj
#         })
