# -*- coding: utf-8 -*-
# from odoo import http


# class Custom/latihan2(http.Controller):
#     @http.route('/custom/latihan2/custom/latihan2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom/latihan2/custom/latihan2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom/latihan2.listing', {
#             'root': '/custom/latihan2/custom/latihan2',
#             'objects': http.request.env['custom/latihan2.custom/latihan2'].search([]),
#         })

#     @http.route('/custom/latihan2/custom/latihan2/objects/<model("custom/latihan2.custom/latihan2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom/latihan2.object', {
#             'object': obj
#         })

