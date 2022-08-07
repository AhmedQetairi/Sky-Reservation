# -*- coding: utf-8 -*-
# from odoo import http


# class SkyCrm(http.Controller):
#     @http.route('/sky_crm/sky_crm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sky_crm/sky_crm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sky_crm.listing', {
#             'root': '/sky_crm/sky_crm',
#             'objects': http.request.env['sky_crm.sky_crm'].search([]),
#         })

#     @http.route('/sky_crm/sky_crm/objects/<model("sky_crm.sky_crm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sky_crm.object', {
#             'object': obj
#         })
