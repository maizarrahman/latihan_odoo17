# from odoo import http


# class Custom/latihan2(http.Controller):
#     @http.route('/latihan', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/latihan/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom/latihan2.listing', {
#             'root': '/custom/latihan2/custom/latihan2',
#             'objects': http.request.env['custom/latihan2.custom/latihan2'].search([]),
#         })

#     @http.route('/latihan/objects/<model("latihan"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom/latihan2.object', {
#             'object': obj
#         })
